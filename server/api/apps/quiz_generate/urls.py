from django.urls import path

from . import views

app_name = "quiz_generate"
urlpatterns = [
    path(
        "generate",
        views.GenerateQuizView.as_view(),
        name="generate_quiz",
    ),
]