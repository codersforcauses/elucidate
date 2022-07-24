from rest_framework import generics
from rest_framework import permissions

from django.utils.timezone import now

from api.apps.shared_models.models.quiz_models import Question, Answer, Subject, Topic
from api.apps.shared_models.serializers import (
    quiz_serializers,
    statistics_serializers,
)


class QuestionDetailView(generics.RetrieveAPIView):
    serializer_class = quiz_serializers.QuestionSerializer
    queryset = Question.objects.all()


class AnswerQuestionListView(generics.ListAPIView):
    serializer_class = quiz_serializers.AnswerSerializer

    def get_queryset(self):
        return Answer.objects.filter(question__pk=self.kwargs["question_pk"])


class AnswerQuestionDetailView(generics.RetrieveAPIView):
    serializer_class = quiz_serializers.AnswerSerializer

    def get_queryset(self):
        return Answer.objects.get(question__pk=self.kwargs["question_pk"],
                                  answer__pk=self.kwargs["answer_pk"])


class SubjectQuestionDetailView(generics.RetrieveAPIView):
    serializer_class = quiz_serializers.SubjectSerializer

    def get_queryset(self):
        return Tag.objects.get(question__pk=self.kwargs["question_pk"]).subject


class TopicQuestionListView(generics.ListAPIView):
    serializer_class = quiz_serializers.TopicSerializer

    def get_queryset(self):
        return Topic.objects.filter(question__pk=self.kwargs["question_pk"])


class QuestionResponseCreateView(generics.CreateAPIView):
    serializer_class = statistics_serializers.QuestionResponseSerializer


class UserStatisticsCreateUpdateView(generics.CreateAPIView, generics.UpdateAPIView):
    serializer_class = statistics_serializers.UserStatisticsSerializer


class QuizStatisticsCreateView(generics.CreateAPIView):
    serializer_class = statistics_serializers.QuizStatisticsSerializer


class QuizTagCreateView(generics.CreateAPIView):
    serializer_class = statistics_serializers.QuizTagSerializer


class QuestionStatisticsCreateView(generics.CreateAPIView):
    serializer_class = statistics_serializers.QuestionStatisticsSerializer


class TopicStatisticsCreateView(generics.CreateAPIView):
    serializer_class = statistics_serializers.TopicStatisticsSerializer
