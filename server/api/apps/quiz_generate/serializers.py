from rest_framework import serializers

from api.apps.shared_models.models.quiz_models import Subject, Topic


class GenerateQuizRequestSerializer(serializers.Serializer):
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())
    topics = serializers.PrimaryKeyRelatedField(
        queryset=Topic.objects.all(), many=True
    )
    question_count = serializers.IntegerField(min_value=1)
    question_types = serializers.DictField(
        child=serializers.BooleanField(),
    )

    class Meta:
        fields = ["subject", "topics", "question_count", "question_types"]
