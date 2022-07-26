from django.contrib.auth import get_user_model
from rest_framework import serializers
from api.apps.shared_models.models.quiz_models import Question, Answer, Topic, Subject
from api.apps.shared_models.models.statistics_models import (
    QuestionResponse,
    UserStatistics,
    QuizStatistics,
    QuestionStatistics,
    TopicStatistics,
)


class QuestionResponseSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all()
    )
    question = serializers.PrimaryKeyRelatedField(
        queryset=Question.objects.all()
    )
    selected_answer = serializers.PrimaryKeyRelatedField(
        queryset=Answer.objects.all()
    )

    class Meta:
        model = QuestionResponse
        fields = [
            "id",
            "user",
            "question",
            "selected_answer",
            "date_submitted",
        ]

    def create(self, validated_data):
        return QuestionResponse.objects.create(**validated_data)


class UserStatisticsSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all()
    )

    class Meta:
        model = UserStatistics
        fields = [
            "id",
            "user",
        ]

    def create(self, validated_data):
        return UserStatistics.objects.create(**validated_data)


class QuizStatisticsSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all()
    )
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())
    topics = serializers.PrimaryKeyRelatedField(queryset=Topic.objects.all(), many=True)

    class Meta:
        model = QuizStatistics
        fields = [
            "id",
            "user",
            "quiz_title",
            "subject",
            "topics",
            "date_taken",
            "score",
        ]

    def create(self, validated_data):
        return QuizStatistics.objects.create(**validated_data)


class QuestionStatisticsSerializer(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(
        queryset=Question.objects.all()
    )

    class Meta:
        model = QuestionStatistics
        fields = [
            "id",
            "question",
        ]

    def create(self, validated_data):
        return QuestionStatistics.objects.create(**validated_data)


class TopicStatisticsSerializer(serializers.ModelSerializer):
    topic = serializers.PrimaryKeyRelatedField(queryset=Topic.objects.all())

    class Meta:
        model = TopicStatistics
        fields = [
            "id",
            "topic",
        ]

    def create(self, validated_data):
        return TopicStatistics.objects.create(**validated_data)
