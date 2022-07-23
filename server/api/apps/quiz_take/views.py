from rest_framework import generics
from rest_framework import permissions

from django.utils.timezone import now

from api.apps.shared_models.models.quiz_models import Question, Answer, Tag
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


class TagQuestionListView(generics.ListAPIView):
    serializer_class = quiz_serializers.TagSerializer

    def get_queryset(self):
        return Tag.objects.filter(question__pk=self.kwargs["question_pk"])


class QuestionResponseCreateView(generics.CreateAPIView):
    serializer_class = statistics_serializers.QuestionResponseSerializer

    def perform_create(self, serializer):
        q = Question.objects.filter(pk=self.kwargs["question_pk"]),
        a = Answer.objects.filter(pk=self.kwargs["selected_answer_pk"]),
        serializer.save(question=q, selected_answer=a, date_submitted=now)
