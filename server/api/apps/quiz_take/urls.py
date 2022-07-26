from django.urls import path

from . import views

app_name = "quiz_take"
urlpatterns = [
    path("question/<int:question_pk>/", views.QuestionDetailView.as_view(), name="question_detail"),
    path("question/<int:question_pk>/answers/", views.AnswerQuestionListView.as_view(), name="answers_list"),
    path(
        "question/<int:question_pk>/answers/<int:answer_pk>",
        views.AnswerQuestionDetailView.as_view(),
        name="answer_detail"
    ),
    path("question/<int:question_pk>/topics/", views.TopicQuestionListView.as_view(), name="topics_list"),
    path("question/<int:question_pk>/topics/<int:topic_pk>", views.TopicQuestionDetailView.as_view(), name="topic_detail"),
    path(
        "question/<int:question_pk>/subject/", views.SubjectQuestionDetailView.as_view(), name="subject_detail",
    ),
    path(
        "submit/question_response/", views.QuestionResponseCreateView.as_view(), name="question_response_create",
    ),
    path("submit/quiz_statistics/", views.QuizStatisticsCreateView.as_view(), name="quiz_statistics_create"),
]
