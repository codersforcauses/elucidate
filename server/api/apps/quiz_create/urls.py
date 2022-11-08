from django.urls import path
from . import views

urlpatterns = [
    path("question/", views.QuestionTask.as_view()),
    path("question/<int:question_pk>/", views.SpecificQuestionTask.as_view()),
    # path("question/<int:question_pk>/answer/", views.AnswerTask.as_view()),
    # path("question/<int:question_pk>/answer/<int:answer_pk>/", views.SpecificAnswerTask.as_view()),
    # path("subject/", views.TagTask.as_view()),
    # path("question/<int:q_pk>/tag/<int:t_pk>/", views.SpecificTagTask.as_view()),
]
