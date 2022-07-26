from tkinter.messagebox import QUESTION
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User
from shared_models.models.statistics_models import QuestionResponse
from shared_models.models.quiz_models import Question
from django.views import generic

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
class UserStatistics(generic.ListView):
    model = QuestionResponse, Question.QuestionType
    queryset = QuestionResponse.objects.filter(user__exact='request.user'), Question.QuestionType.objects.filter(creator__exact='request.creator')
    context_object_name = 'user_answered_question_and_made_quizzes'
    #template_name: template_name/location
    
    
    
    

