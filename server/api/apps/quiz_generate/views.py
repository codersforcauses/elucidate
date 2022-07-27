from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions

from . import serializers

from api.apps.shared_models.models.quiz_models import Answer, Question, Topic
from api.apps.shared_models.serializers import (
    quiz_serializers,
    statistics_serializers,
)

class QuestionDetailView(generics.RetrieveAPIView):
    """GET request to return information about a specific question"""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = quiz_serializers.QuestionSerializer
    queryset = Question.objects.all()
    lookup_url_kwarg = "question_pk"