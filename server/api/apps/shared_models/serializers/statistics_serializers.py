from rest_framework import serializers
from ..models.statistics_models import QuestionResponse, UserStatistics, QuizStatistics, QuizTag


class QuestionResponseSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField()
    question = serializers.PrimaryKeyRelatedField()
    selected_answer = serializers.PrimaryKeyRelatedField()

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
    user = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = UserStatistics
        fields = [
            "id",
            "user",
            "quizzes_completed",
            "average_score",
        ]

    def create(self, validated_data):
        return UserStatistics.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get("user", instance.user)
        instance.quizzes_completed = validated_data.get("quizzes_completed", instance.quizzes_completed)
        instance.average_score = validated_data.get("average_score", instance.average_score)
        return instance


class QuizStatisticsSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField()

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
    quiz_statistics = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = QuizTag
        fields = [
            "id",
            "name",
            "quiz_statistics",
        ]

    def create(self, validated_data):
        return QuizTag.objects.create(**validated_data)
