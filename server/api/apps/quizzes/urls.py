from django.urls import path
from . import views

urlpatterns = [
    path("", views.QuizCreateListView.as_view(), name="quizzes"),
    path("<int:pk>/", views.QuizDetailView.as_view(), name="quiz-detail"),
    path(
        "user/<int:user_pk>/quizzes/",
        views.UserQuizListView.as_view(),
        name="user-quizzes",
    ),
    path(
        "user/<int:user_pk>/quiz/<int:quiz_pk>/",
        views.UserQuizDetail.as_view(),
        name="user-quiz-detail",
    ),
]
