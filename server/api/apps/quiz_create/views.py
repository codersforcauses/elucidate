from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializers import QuestionInfoSerializer
from api.apps.shared_models.models import quiz_models
from api.apps.shared_models.serializers import quiz_serializers
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
)
from .permissions
from django.contrib.auth import get_user_model
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt  # will change this later

# this method associates a tag with a question or adds a new tag to the
# database and returns the Tag object
def AddTagToQuestion(question, tag_name):
    try:
        tag = quiz_models.Tag.objects.get(name=tag_name)
        question.tag_set.add(tag)
    except quiz_models.Tag.DoesNotExist:
        tag = question.tag_set.create(name=tag_name)
    except quiz_models.Tag.MultipleObjectsReturned:
        # hopefully this shouldn't be executed in production
        tag = quiz_models.Tag.objects.filter(name=tag_name)[0]
        question.tag_set.add(tag)
    return tag
    

class QuestionTask(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = quiz_serializers.QuestionSerializer
    queryset = quiz_models.Question.objects.all()
    def post(self, request):
        serializer = QuestionInfoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            question = quiz_models.Question(
                text=serializer.data["text"],
                question_type=serializer.data["question_type"],
                date_created=serializer.data["date_created"],
            )
            question.save()

            if "answers" in serializer.data:
                for answer in serializer.data["answers"]:
                    # vaildate fields as the serialiser doesn't verify them
                    if type(answer[0]) is str and type(answer[1]) is bool:
                        question.answer_set.create(
                            text=answer[0], is_correct=answer[1]
                        )
                    else:
                        return Response(status=status.HTTP_400_BAD_REQUEST)

            for name in serializer.data["tags"]:
                AddTagToQuestion(question, name)

            return Response(
                quiz_serializers.QuestionSerializer(question).data,
                status=status.HTTP_201_CREATED,
            )


class SpecificQuestionTask(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser | IsOwner]
    serializer_class = quiz_serializers.QuestionSerializer
    model = quiz_models.Question
    
    def get_object(self):
        obj_pk = self.kwargs['q_pk']
        return quiz_models.Question.objects.get(pk=obj_pk)
    
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class AnswerTask(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated | IsOwner]
    serializer_class = quiz_serializers.AnswerSerializer
    
    def get_queryset(self):
        obj_pk = self.kwargs['q_pk']
        return quiz_models.Question.objects.get(pk=obj_pk).answer_set.all()
    
    def post(self, request, q_pk): 
        question = quiz_models.Question.objects.get(pk=q_pk)
        serializer = quiz_serializers.AnswerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            answer = question.answer_set.create(
                text=serializer.data["text"],
                is_correct=serializer.data["is_correct"],
            )
            return Response(quiz_serializers.AnswerSerializer(answer).data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)



class SpecificAnswerTask(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser | IsOwner]
    serializer_class = quiz_serializers.AnswerSerializer
    
    def get_object(self):
        question_pk = self.kwargs['q_pk']
        answer_pk = self.kwargs['a_pk']
        return quiz_models.Question.objects.get(pk=question_pk).answer_set.get(pk=answer_pk)
    
    def put(self, request, *args, **kwargs):
        obj_pk = self.kwargs['q_pk']
        return self.partial_update(request, *args, **kwargs)


class TagTask(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser | IsOwner]
    serializer_class = quiz_serializers.TagSerializer
    
    def get_queryset(self):
        return quiz_models.Question.objects.get(pk=self.kwargs['q_pk']).tag_set.all()
    
    def post(self, request, q_pk): 
        question = quiz_models.Question.objects.get(pk=q_pk)
        serializer = quiz_serializers.TagSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            tag = AddTagToQuestion(question, serializer.data["name"])
            return Response(quiz_serializers.TagSerializer(tag).data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class SpecificTagTask(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAdminUser | IsOwner]
    serializer_class = quiz_serializers.TagSerializer
    model = quiz_models.Tag
    
    def get_object(self):
        return quiz_models.Question.objects.get(pk=self.kwargs['q_pk']).tag_set.get(pk=self.kwargs['t_pk'])
    
    def delete(self, request):
        question = quiz_models.Question.objects.get(pk=self.kwargs['q_pk'])
        question.tag_set.remove(self.get_object())
        return Response(status=status.HTTP_204_NO_CONTENT)