from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from api.apps.quizzes.models import Quiz
from api.apps.shared_models.models.quiz_models import Answer, Question, Topic
from api.apps.shared_models.models.statistics_models import QuestionResponse
from api.apps.quizzes.views import IsOwner
from api.apps.shared_models.serializers import (
    question_serializers,
    statistics_serializers,
)
from rest_framework.response import Response
from rest_framework import status


class QuestionDetailView(generics.RetrieveAPIView):
    """GET request to return information about a specific question"""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = question_serializers.QuestionSerializer
    queryset = Question.objects.all()
    lookup_url_kwarg = "question_pk"


class AnswerQuestionListView(generics.ListAPIView):
    """
    GET request to return a list of answers associated with a specific question
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = question_serializers.AnswerSerializer

    def get_queryset(self):
        return Answer.objects.filter(question__pk=self.kwargs["question_pk"])


class AnswerQuestionDetailView(generics.RetrieveAPIView):
    """
    GET request to return information about a specific answer associated to a
    specific question
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = question_serializers.AnswerSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        self.check_object_permissions(self.request, obj)
        return obj

    def get_queryset(self):
        return Answer.objects.filter(
            question__pk=self.kwargs["question_pk"],
            pk=self.kwargs["answer_pk"],
        )


class SubjectQuestionDetailView(generics.RetrieveAPIView):
    """
    GET request to return information about the subject associated to a
    specific question
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = question_serializers.SubjectSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        self.check_object_permissions(self.request, obj)
        return obj.subject

    def get_queryset(self):
        return Question.objects.filter(pk=self.kwargs["question_pk"])


class TopicQuestionListView(generics.ListAPIView):
    """
    GET request to return a list of topics associated to a specific question
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = question_serializers.TopicSerializer

    def get_queryset(self):
        return Topic.objects.filter(
            question__pk=self.kwargs["question_pk"]
        ).order_by("id")


class TopicQuestionDetailView(generics.RetrieveAPIView):
    """
    GET request to return information about a specific topic associated to a
    specific question
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = question_serializers.TopicSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        self.check_object_permissions(self.request, obj)
        return obj

    def get_queryset(self):
        return Topic.objects.filter(
            question__pk=self.kwargs["question_pk"], pk=self.kwargs["topic_pk"]
        )


class QuestionResponseListView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = statistics_serializers.QuestionResponseListSerializer
    queryset = QuestionResponse.objects.all()

    def get(self, request, quiz_pk):
        qs = self.queryset.all().filter(quiz=quiz_pk, user=request.user)
        serializer = self.serializer_class(instance=qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class QuestionResponseDetailsView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = statistics_serializers.QuestionResponseDetailsSerializer
    queryset = QuestionResponse.objects.all()

    def get(self, request, quiz_pk, question_pk):
        qs = self.queryset.all().filter(quiz=quiz_pk, user=request.user)
        qr = qs.get(question=question_pk)
        serializer = self.serializer_class(instance=qr)
        return Response(serializer.data, status=status.HTTP_200_OK)


class QuestionResponseCreateUpdateView(generics.GenericAPIView):
    """
    POST request to create a QuestionResponse for a user, upon submitting a
    question
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = statistics_serializers.QuestionResponseSerializer
    queryset = QuestionResponse.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        user = request.user
        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request):
        qs = self.queryset.all().filter(
            quiz=request.data.get("quiz"), user=request.user
        )
        qr = qs.get(question=request.data.get("question"))
        qr.selected_answer = request.data.get("selected_answer")
        qr.save()
        serializer = self.get_serializer(qr)
        return Response(serializer.data)


class QuizStatisticsCreateView(generics.CreateAPIView):
    """
    POST request to create a QuizStatistics entry for a user, upon creating a
    quiz
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = statistics_serializers.QuizStatisticsSerializer


class SubmitView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated | IsOwner]

    def post(self, request, quiz_id):
        quiz = Quiz.objects.get(id=quiz_id)
        quiz.completed = True
        quiz.save()
        
        # TODO: MARK EACH QUESTION
        return Response(status=status.HTTP_200_OK)
