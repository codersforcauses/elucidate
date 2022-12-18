from django.contrib.auth import get_user_model
from rest_framework import serializers

from api.apps.shared_models.serializers.question_serializers import (
    QuestionSerializer,
    TopicSerializer,
)

from .models import Quiz

User = get_user_model()


class QuizCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ["questions", "topics"]


class QuizDetailSerializer(serializers.ModelSerializer):
    # created_at = serializers.DateTimeField()
    # updated_at = serializers.DateTimeField()
    # attempts = serializers.IntegerField(default=0)
    # correct = serializers.IntegerField(default=0)
    topics = TopicSerializer(many=True)
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = [
            "id",
            "questions",
            "topics"
            # "created_at",
            # "updated_at",
            # "attempts",
            # "creator",
        ]
