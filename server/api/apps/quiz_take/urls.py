from django.urls import path

from . import views

app_name = "quiz_take"
urlpatterns = [
    path("<int:question_pk>/", views.QuestionDetailView.as_view()),
    path("<int:question_pk>/answers/", views.AnswerQuestionListView.as_view()),
    path("<int:question_pk>/answers/<int:answer_pk>",
         views.AnswerQuestionDetailView.as_view()),
    path("<int:question_pk>/tags/", views.TagQuestionListView.as_view()),
]

