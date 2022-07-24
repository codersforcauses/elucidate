from django.contrib.auth import get_user_model
from rest_framework import serializers
from ..models.quiz_models import Question, Answer
from ..models.statistics_models import QuestionResponse, UserStatistics, QuizStatistics, QuizTag


class QuestionResponseSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())
    selected_answer = serializers.PrimaryKeyRelatedField(queryset=Answer.objects.all())

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
    user = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())

    class Meta:
        model = UserStatistics
        fields = [
            "id",
            "user",
            "quizzes_completed",
        ]

    def create(self, validated_data):
        return UserStatistics.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get("user", instance.user)
        instance.quizzes_completed = validated_data.get("quizzes_completed", instance.quizzes_completed)
        return instance


class QuizStatisticsSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())

    class Meta:
        model = QuizStatistics
        fields = [
            "id",
            "user",
            "quiz_title",
            "date_taken",
            "score",
        ]

    def create(self, validated_data):
        return QuizStatistics.objects.create(**validated_data)


class QuizTagSerializer(serializers.ModelSerializer):
    quiz_statistics = serializers.PrimaryKeyRelatedField(queryset=QuizStatistics.objects.all())

    class Meta:
        model = QuizTag
        fields = [
            "id",
            "name",
            "quiz_statistics",
        ]

    def create(self, validated_data):
        return QuizTag.objects.create(**validated_data)
