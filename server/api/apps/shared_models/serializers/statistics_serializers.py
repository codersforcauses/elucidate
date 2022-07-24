from rest_framework import serializers
from ..models.statistics_models import QuestionResponse, UserStatistics, QuizStatistics, QuizTag


class QuestionResponseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestionResponse
        fields = [
            "id",
            "user",
            "question",
            "selected_answer",
            "date_submitted",
        ]
        # TODO: look into ForeignKey / ManyToManyField serialisation

    def create(self, validated_data):
        return QuestionResponse.objects.create(**validated_data)


class UserStatisticsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserStatistics
        fields = [
            "id",
            "user",
            "quizzes_completed",
            "average_score",
        ]
        # TODO: look into foreikjdfjlksadjflsadjf;/ ...

    def create(self, validated_data):
        return UserStatistics.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get("user", instance.user)
        instance.quizzes_completed = validated_data.get("quizzes_completed", instance.quizzes_completed)
        instance.average_score = validated_data.get("average_score", instance.average_score)
        return instance


class QuizStatisticsSerializer(serializers.HyperlinkedModelSerializer):
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


class QuizTagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuizTag
        fields = [
            "id",
            "name",
            "quiz_statistics",
        ]

    def create(self, validated_data):
        return QuizTag.objects.create(**validated_data)
