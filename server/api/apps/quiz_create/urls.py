from django.urls import path

from . import views

urlpatterns = [
    path('question/', views.QuestionTask),
    path('question/<int:question_pk>/', views.SpecificQuestionTask),
    path('question/<int:question_pk>/answer/', views.AnswerTask),
    path('question/<int:question_pk>/answer/<int:answer_pk>', views.SpecificAnswerTask),
    path('question/<int:question_pk>/tag', views.TagTask),
]