from django.urls import path

from .views import EmailResetLinkView, ResetPasswordView

urlpatterns = [
    path("email/", EmailResetLinkView.as_view(), name="send-reset-email"),
    path(
        "",
        ResetPasswordView.as_view(),
        name="reset",
    ),
]
