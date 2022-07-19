from rest_framework import serializers
from .models import Quiz_Question, Question_Answer, Question_Tag
from .defines import QUIZ_QUESTION_MAXLEN, QUIZ_TAG_MAXLEN


class QuestionInfoSerializer(serializers.Serializer):
    question_type = serializers.IntegerField()
    question = serializers.CharField(max_length=QUIZ_QUESTION_MAXLEN)
    date_created = serializers.DateTimeField()
    tags = serializers.ListField(
        child=serializers.CharField(max_length=QUIZ_TAG_MAXLEN)
        )


class Quiz_QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quiz_Question
        fields = ['id', 'question_type', 'question', 'date_created']


class Question_AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question_Answer
        fields = ['id', 'is_correct', 'answer']


class Question_TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question_Tag
        fields = ['id', 'tag']
