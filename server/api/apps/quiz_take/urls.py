from django.urls import path

from . import views

urlpatterns = [
    path("quiz/<int:quiz_pk>/", views.quiz),
    path("quiz/<int:quiz_pk>/objectives/", views.objectives),
    path("quiz/<int:quiz_pk>/tags/", views.tags),
    path("quiz/<int:quiz_pk>/questions/<int:question_pk>/", views.question),
    path("quiz/<int:quiz_pk>/questions/<int:question_pk>/answers/",
         views.answers),
]

