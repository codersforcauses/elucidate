from django.urls import include, path
from django.contrib.auth import views
from .views import ChangePasswordView
from .views import PasswordReset


urlpatterns = [
    # path("", views.PasswordResetView.as_view()),
    path("", PasswordReset.as_view()),
    path("<str:token>/", ChangePasswordView.as_view(),  name = "reset-password" )

]
