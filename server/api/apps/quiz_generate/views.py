from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from . import serializers
from api.apps.shared_models.models.quiz_models import Question, Topic, Subject


class GenerateQuizView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.GenerateQuizRequestSerializer
    
    def get_queryset(self):
        return Question.objects.filter(
            subject=self.kwargs["subject"],
            topics=self.kwargs["topics"],
            question_type=self.kwargs["question_type"]
        )