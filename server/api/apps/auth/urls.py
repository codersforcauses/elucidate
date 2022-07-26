from django.urls import path
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token,
)

from .views import RegistrationView

urlpatterns = [
    path("login/", obtain_jwt_token, name="get-jwt-token"),
    path("refresh/", refresh_jwt_token, name="refresh-jwt-token"),
    path("verify/", verify_jwt_token, name="verify-jwt-token"),
    path("register/", RegistrationView.as_view(), name="register"),
]
