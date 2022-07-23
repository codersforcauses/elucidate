from .models import Quiz
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class QuizCreationSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    question = serializers.CharField(max_length=200)
    answer = serializers.CharField(max_length=200)
    category = serializers.CharField(max_length=100, default="General")

    class Meta:
        model = Quiz
        fields = ["id", "title", "question", "answer", "category"]


class QuizDetailSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    question = serializers.CharField(max_length=200)
    answer = serializers.CharField(max_length=200)
    category = serializers.CharField(max_length=100, default="General")
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    attempts = serializers.IntegerField(default=0)
    correct = serializers.IntegerField(default=0)

    class Meta:
        model = Quiz
        fields = [
            "id",
            "title",
            "question",
            "answer",
            "category",
            "created_at",
            "updated_at",
            "correct",
            "attempts",
            "creator",
        ]
