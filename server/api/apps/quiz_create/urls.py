from django.urls import path
from . import views

urlpatterns = [
    path('question/', views.QuestionTask),
    path('question/<int:q_pk>/', views.SpecificQuestionTask),
    path('question/<int:q_pk>/answer/', views.AnswerTask),
    path('question/<int:q_pk>/answer/<int:a_pk>', views.SpecificAnswerTask),
    path('question/<int:q_pk>/tag/', views.TagTask),
    path('question/<int:q_pk>/tag/<int:t_pk>', views.SpecificTagTask),
]
