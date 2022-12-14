from django.urls import path

from . import views

app_name = "quiz_generate"
urlpatterns = [
    path(
        "generate/",
        views.GenerateQuizView.as_view(),
    ),
    # path(
    #     "subject-exists",
    #     views.SubjectExistsView.as_view(),
    #     name="subject-exists",
    # ),
    # path(
    #     "topic-exists",
    #     views.TopicExistsView.as_view(),
    #     name="topic-exists",
    # ),
]
