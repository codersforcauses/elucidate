from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions

from api.apps.shared_models.models.quiz_models import Answer, Question, Topic
from api.apps.shared_models.serializers import (
    question_serializers,
    statistics_serializers,
)


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
        return Topic.objects.filter(question__pk=self.kwargs["question_pk"])


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


class QuestionResponseCreateView(generics.CreateAPIView):
    """
    POST request to create a QuestionResponse for a user, upon submitting a
    question
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = statistics_serializers.QuestionResponseSerializer


class QuizStatisticsCreateView(generics.CreateAPIView):
    """
    POST request to create a QuizStatistics entry for a user, upon creating a
    quiz
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = statistics_serializers.QuizStatisticsSerializer
