from rest_framework import generics
from rest_framework import permissions

from django.utils.timezone import now

from api.apps.shared_models.models.quiz_models import (
    Question,
    Answer,
    Subject,
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


class AnswerQuestionListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = quiz_serializers.AnswerSerializer

    def get_queryset(self):
        return Answer.objects.filter(question__pk=self.kwargs["question_pk"])


class AnswerQuestionDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = quiz_serializers.AnswerSerializer

    def get_queryset(self):
        return Answer.objects.get(
            question__pk=self.kwargs["question_pk"],
            answer__pk=self.kwargs["answer_pk"],
        )


class SubjectQuestionDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = quiz_serializers.SubjectSerializer

    def get_queryset(self):
        return Question.objects.get(pk=self.kwargs["question_pk"]).subject


class TopicQuestionListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = quiz_serializers.TopicSerializer

    def get_queryset(self):
        return Topic.objects.filter(question__pk=self.kwargs["question_pk"])


class TopicQuestionDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = quiz_serializers.TopicSerializer

    def get_queryset(self):
        return Topic.objects.get(question__pk=self.kwargs["question_pk"], pk=self.kwargs["topic_pk"])


class QuestionResponseCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = statistics_serializers.QuestionResponseSerializer


class QuizStatisticsCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = statistics_serializers.QuizStatisticsSerializer

    def perform_create(self, serializer):
        userstats = UserStatistics.objects.get(user=serializer.user)
        userstats.quizzes_completed += 1
        userstats.save()
        serializer.save()
