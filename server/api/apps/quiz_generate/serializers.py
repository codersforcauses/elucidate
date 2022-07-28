from rest_framework import serializers
from api.apps.shared_models.models.quiz_models import (
    Question,
    Subject,
    Topic,
)


class GenerateQuizRequestSerializer(serializers.Serializer):
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())
    topics = serializers.PrimaryKeyRelatedField(queryset=Topic.objects.all(), many=True)
    question_count = serializers.IntegerField(min_value=1)
    question_type = serializers.MultipleChoiceField(choices=Question.QuestionType.choices)

    class Meta:
        fields = [
            "subject",
            "topics",
            "question_count",
            "question_type",
        ]


class GenerateQuizResponseSerializer(serializers.Serializer):
    pk_array = serializers.ListField(child=serializers.PrimaryKeyRelatedField(queryset=Question.objects.all()))

    class Meta:
        model = Question
        fields = [
            "pk_array",
        ]
