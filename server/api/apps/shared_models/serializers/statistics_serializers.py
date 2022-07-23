from rest_framework import serializers
from ..models.statistics_models import QuestionResponse


class QuestionResponseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestionResponse
        fields = [
            "id",
            "question",
            "selected_answer",
            "date_submitted",
        ]
