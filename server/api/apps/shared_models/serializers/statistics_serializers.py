from rest_framework import serializers
from ..models.statistics_models import QuestionResponse


class QuestionResponseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestionResponse
        fields = [
            "id",
            "question_count",
            "total_marks",
            "user_mark",
            "time_taken",
            "date_taken",
        ]
