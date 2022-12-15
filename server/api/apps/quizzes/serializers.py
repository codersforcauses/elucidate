from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Quiz

User = get_user_model()


class QuizCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ["questions", "topic"]


class QuizDetailSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    attempts = serializers.IntegerField(default=0)
    correct = serializers.IntegerField(default=0)

    class Meta:
        model = Quiz
        fields = [
            "questions",
            "created_at",
            "updated_at",
            "attempts",
            "creator",
        ]
