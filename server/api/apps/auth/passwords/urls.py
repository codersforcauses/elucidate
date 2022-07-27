from django.urls import path
from .views import ChangePasswordView
from .views import PasswordReset


urlpatterns = [
    path("", PasswordReset.as_view()),
    path("<str:token>/", ChangePasswordView.as_view(), name="reset-password")
]
