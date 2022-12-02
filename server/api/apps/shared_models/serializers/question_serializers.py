from django.contrib.auth import get_user_model
from rest_framework import serializers

from api.apps.shared_models.models.quiz_models import (
    Answer,
    Question,
    Subject,
    Topic,
)


class QuestionSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all()
    )
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())
    topics = serializers.PrimaryKeyRelatedField(
        queryset=Topic.objects.all(), many=True
    )

    class Meta:
        model = Question
        fields = [
            "question",
            "question_type",
            "marks",
            "creator",
            "date_created",
            "subject",
            "topics",
        ]


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ["name"]


class TopicSerializer(serializers.ModelSerializer):
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())

    class Meta:
        model = Topic
        fields = ["name", "subject"]


class AnswerSerializer(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(
        queryset=Question.objects.all()
    )

    class Meta:
        model = Answer
        fields = ["answer", "is_correct", "question"]

    def create(self, validated_data):
        return Answer.objects.create(**validated_data)
