from rest_framework import routers, serializers, viewsets
from .models import *


class QuizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quiz
        fields = ["id", "name", "subject", "time_limit", "date_created"]


class ObjectiveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Objective
        fields = ["id", "name", "quiz"]


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name", "quiz"]


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "text", "quiz"]

        
class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ["id", "text", "question"]

