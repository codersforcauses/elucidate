from rest_framework import generics
from rest_framework import permissions

from api.apps.shared_models.models.quiz_models import Question, Answer, Tag
from api.apps.shared_models.serializers import quiz_serializers


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
