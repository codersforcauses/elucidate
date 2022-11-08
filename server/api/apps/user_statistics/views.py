from django.shortcuts import render
from rest_framework import generics, permissions
from api.apps.shared_models.serializers import statistics_serializers, quiz_serializers
from api.apps.shared_models.models import statistics_models, quiz_models

# Create your views here.
class UserStatisticsDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = statistics_serializers.UserStatisticsSerializer
    lookup_url_kwarg = "user_pk"

    def get_queryset(self):
        return statistics_models.UserStatistics.objects.filter(
            user__pk=self.kwargs["user_pk"]
        )
class QuizStatisticsListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = statistics_serializers.QuizStatisticsSerializer
    
    def get_queryset(self):
        return statistics_models.QuizStatistics.objects.filter(
            user__pk=self.kwargs["user_pk"]
        )

class QuestionListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = quiz_serializers.QuestionSerializer

    def get_queryset(self):
        return quiz_models.Question.objects.filter(
            creator__pk=self.kwargs["user_pk"]
        )
