from rest_framework import generics
from rest_framework import permissions

from django.shortcuts import get_object_or_404

from api.apps.shared_models.models.quiz_models import (
    Question,
    Answer,
    Topic,
)
from api.apps.shared_models.serializers import (
    quiz_serializers,
    statistics_serializers,
)


class QuestionDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = quiz_serializers.QuestionSerializer
    queryset = Question.objects.all()
    lookup_url_kwarg = "question_pk"


class AnswerQuestionListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = quiz_serializers.AnswerSerializer

    def get_queryset(self):
        return Answer.objects.filter(question__pk=self.kwargs["question_pk"])


class AnswerQuestionDetailView(
    generics.RetrieveAPIView, generics.CreateAPIView
):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = quiz_serializers.AnswerSerializer

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
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = quiz_serializers.SubjectSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        self.check_object_permissions(self.request, obj)
        return obj.subject

    def get_queryset(self):
        return Question.objects.filter(pk=self.kwargs["question_pk"])


class TopicQuestionListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = quiz_serializers.TopicSerializer

    def get_queryset(self):
        return Topic.objects.filter(question__pk=self.kwargs["question_pk"])


class TopicQuestionDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = quiz_serializers.TopicSerializer

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
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = statistics_serializers.QuestionResponseSerializer


class QuizStatisticsCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = statistics_serializers.QuizStatisticsSerializer
