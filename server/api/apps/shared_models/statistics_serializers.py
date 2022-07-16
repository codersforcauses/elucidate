from rest_framework import routers, serializers, viewsets
from models.statistics_models import *


class QuestionResponseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestionResponse
        fields = ["id",
                  "question",
                  "selected_answer",
                  "is_correct",
                  "time_taken",
                  "date_created"]

