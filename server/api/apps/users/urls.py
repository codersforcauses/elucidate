from django.urls import path, include
from rest_framework import routers
from . import views


urlpatterns = [
    path("signup/", views.UserCreateView.as_view(), name="sign_up"),
    path(
        "api-auth/", include("rest_framework.urls", namespace="rest_framework")
    ),
]
