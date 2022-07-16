from django.urls import path

from . import views

app_name = "shared_models"
urlpatterns = [
    path("<int:question_pk>/", views.question),
    path("<int:question_pk>/tags/", views.tags),
    path("<int:question_pk>/answers/", views.answers),
]

