from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from api.apps.quizzes.views import IsOwner
from api.apps.shared_models.models import quiz_models
from api.apps.shared_models.serializers import quiz_serializers

from . import serializers


class QuestionTask(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.QuestionInfoSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            question = quiz_models.Question(
                text=serializer.data["text"],
                question_type=serializer.data["question_type"],
                marks=serializer.data["marks"],
                subject=get_object_or_404(
                    quiz_models.Subject, pk=serializer.data["subject"]
                ),
                creator=request.user,
            )
            question.save()

            for topic in serializer.data["topics"]:
                question.topics.add(
                    get_object_or_404(quiz_models.Topic, pk=topic)
                )

            for answer in serializer.data["answers"]:
                # vaildate fields as the serialiser doesn't verify them
                if type(answer[0]) is str and type(answer[1]) is bool:
                    question.answer_set.create(
                        text=answer[0], is_correct=answer[1]
                    )
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)

            return Response({"pk": question.pk})


class SpecificQuestionTask(generics.RetrieveUpdateDestroyAPIView):
    """
    Currently only admins can view specific questions, as django doesn't
    support easily method specific permissions. Might need to change later
    if required.
    """

    permission_classes = [permissions.IsAdminUser]
    serializer_class = quiz_serializers.QuestionSerializer
    model = quiz_models.Question

    def get_object(self):
        obj_pk = self.kwargs["question_pk"]
        return get_object_or_404(quiz_models.Question.objects, pk=obj_pk)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class AnswerTask(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated | IsOwner]
    serializer_class = quiz_serializers.AnswerSerializer

    def get_queryset(self):
        obj_pk = self.kwargs["q_pk"]
        return quiz_models.Question.objects.get(pk=obj_pk).answer_set.all()

    def post(self, request, q_pk):
        question = quiz_models.Question.objects.get(pk=q_pk)
        serializer = quiz_serializers.AnswerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            answer = question.answer_set.create(
                text=serializer.data["text"],
                is_correct=serializer.data["is_correct"],
            )
            return Response(
                quiz_serializers.AnswerSerializer(answer).data,
                status=status.HTTP_201_CREATED,
            )
        return Response(status=status.HTTP_400_BAD_REQUEST)


class SpecificAnswerTask(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser | IsOwner]
    serializer_class = quiz_serializers.AnswerSerializer

    def get_object(self):
        question_pk = self.kwargs["q_pk"]
        answer_pk = self.kwargs["a_pk"]
        return quiz_models.Question.objects.get(pk=question_pk).answer_set.get(
            pk=answer_pk
        )

    def put(self, request, *args, **kwargs):
        obj_pk = self.kwargs["q_pk"]
        return self.partial_update(request, *args, **kwargs)


# class TagTask(generics.ListCreateAPIView):
#     permission_classes = [IsAdminUser | IsOwner]
#     serializer_class = quiz_serializers.TagSerializer

#     def get_queryset(self):
#         return quiz_models.Question.objects.get(
#             pk=self.kwargs["q_pk"]
#         ).tag_set.all()

#     def post(self, request, q_pk):
#         question = quiz_models.Question.objects.get(pk=q_pk)
#         serializer = quiz_serializers.TagSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             tag = AddTagToQuestion(question, serializer.data["name"])
#             return Response(
#                 quiz_serializers.TagSerializer(tag).data,
#                 status=status.HTTP_201_CREATED,
#             )
#         return Response(status=status.HTTP_400_BAD_REQUEST)


# class SpecificTagTask(generics.RetrieveDestroyAPIView):
#     permission_classes = [IsAdminUser | IsOwner]
#     serializer_class = quiz_serializers.TagSerializer
#     model = quiz_models.Tag

#     def get_object(self):
#         return quiz_models.Question.objects.get(
#             pk=self.kwargs["q_pk"]
#         ).tag_set.get(pk=self.kwargs["t_pk"])

#     def delete(self, request):
#         question = quiz_models.Question.objects.get(pk=self.kwargs["q_pk"])
#         question.tag_set.remove(self.get_object())
#         return Response(status=status.HTTP_204_NO_CONTENT)
