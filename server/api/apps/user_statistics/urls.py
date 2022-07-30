from django.urls import path
from . import views

app_name = "user_statistics"
urlpatterns = [
    path(
        "user/<int:user_pk>/",
        views.UserStatisticsDetailView.as_view(),
        name="stats",
    ),
    path("user/<int:user_pk>/quiz_list/",views.QuizStatisticsListView.as_view(),name="quiz-list"),
    path("user/<int:user_pk>/question_list/",views.QuestionListView.as_view(), name="question-list")
]
