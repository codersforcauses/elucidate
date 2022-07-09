from django.urls import path

from . import views

urlpatterns = [
    path('quiz/', views.QuizTask),
    path('quiz/<int:pk>/', views.SpecificQuizTask),
    # path('quiz/<int:pk>/answer/', views.SpecificAnswerTask),
    # path('quiz/<int:pk>/answer/<int:pk>', views.SpecificAnswerTask),
    # path('quiz/<int:pk>/question/', views.SpecificAnswerTask),
    # path('quiz/<int:pk>/question/<int:pk>', views.SpecificAnswerTask),
]