from django.urls import path

from . import views

app_name = "quiz_take"
urlpatterns = [
    path("<int:quiz_pk>/", views.quiz),
    path("<int:quiz_pk>/objectives/", views.objectives),
    path("<int:quiz_pk>/tags/", views.tags),
    path("<int:quiz_pk>/questions/<int:question_pk>/", views.question),
    path("<int:quiz_pk>/questions/<int:question_pk>/answers/",
         views.answers),
]

