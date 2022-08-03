from rest_framework import serializers
from api.apps.shared_models.models.quiz_models import (
    Question,
    Subject,
    Topic,
)


class QuestionInfoSerializer(serializers.Serializer):
    text = serializers.CharField()
    question_type = serializers.ChoiceField(
        choices=Question.QuestionType.choices
        )
    marks = serializers.IntegerField(min_value=1)
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())
    topics = serializers.PrimaryKeyRelatedField(
        queryset=Topic.objects.all(), many=True
    )
    answers = serializers.ListField(
        child=(
            serializers.ListField(  # will vailidate types in views
                allow_empty=False, min_length=2, max_length=2
            )
        )
    )
