from django.urls import path

from . import views

app_name = "quiz_take"
urlpatterns = [
    path(
        "question/<int:question_pk>/",
        views.QuestionDetailView.as_view(),
        name="question_detail",
    ),
    path(
        "question/<int:question_pk>/topics/",
        views.TopicQuestionListView.as_view(),
        name="topics_list",
    ),
    path(
        "question/<int:question_pk>/topics/<int:topic_pk>",
        views.TopicQuestionDetailView.as_view(),
        name="topic_detail",
    ),
    path(
        "question/<int:question_pk>/subject/",
        views.SubjectQuestionDetailView.as_view(),
        name="subject_detail",
    ),
    path(
        "save/<int:quiz_pk>/",
        views.QuestionResponseListView.as_view(),
        name="question_response_list",
    ),
    path(
        "save/<int:quiz_pk>/<int:question_pk>/",
        views.QuestionResponseDetailsView.as_view(),
        name="question_response_details",
    ),
    path(
        "save/",
        views.QuestionResponseCreateUpdateView.as_view(),
        name="question_response_create_update",
    ),
    path(
        "submit/quiz_statistics/",
        views.QuizStatisticsCreateView.as_view(),
        name="quiz_statistics_create",
    ),
]
