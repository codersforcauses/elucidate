from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User
from shared_models.models.statistics_models import QuizStatistics
from shared_models.models.quiz_models import Question, Tag, Answer
from django.views import generic

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
class UserStatistics(generic.ListView):
    model = QuizStatistics
    
    
    

