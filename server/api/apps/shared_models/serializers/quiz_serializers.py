from rest_framework import serializers
from ..models.quiz_models import Question, Tag, Answer


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "text", "question_type", "date_created"]


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ["id", "text", "is_correct"]
