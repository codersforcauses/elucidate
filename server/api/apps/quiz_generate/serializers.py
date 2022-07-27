from rest_framework import serializers
from api.apps.shared_models.models.quiz_models import (
    Answer,
    Question,
    Subject,
    Topic,
)


class GenerateQuizRequestSerializer(serializers.ModelSerializer):
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())
    topics = serializers.PrimaryKeyRelatedField(queryset=Topic.objects.all(), many=True)
    question_count = 

    class Meta:
        model = Question
        fields = [
            "text",
            "question_type",
            "marks",
            "creator",
            "date_created",
            "subject",
            "topics",
            "is_verified",
        ]


class GenerateQuizResponseSerializer(serializers.ModelSerializer):
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())
    topics = serializers.PrimaryKeyRelatedField(
        queryset=Topic.objects.all(), many=True
    )

    class Meta:
        model = Question
        fields = [
            "text",
            "question_type",
            "marks",
            "creator",
            "date_created",
            "subject",
            "topics",
            "is_verified",
        ]
