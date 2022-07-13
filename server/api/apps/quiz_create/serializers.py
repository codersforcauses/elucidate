from rest_framework import routers, serializers, viewsets
from .models import *

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