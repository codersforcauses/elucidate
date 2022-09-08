from smtplib import SMTPAuthenticationError

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import ChangePasswordSerializer, EmailSerializer


# Create your views here.
class ResetPasswordView(generics.RetrieveUpdateAPIView):
    """
    An endpoint for changing password.
    """

    serializer_class = ChangePasswordSerializer

    def validate_token(self, request):
        token = request.GET.get("token", "").rstrip("/")
        uid = None
        try:
            uidb64 = request.GET.get("uid", "").rstrip("/")
            if uidb64 != "":
                uid = force_str(urlsafe_base64_decode(uidb64))
        except ValueError:
            pass

        user = get_user_model().objects.filter(email=uid).first()

        is_valid_token = PasswordResetTokenGenerator().check_token(
            token=token, user=user
        )
        return is_valid_token

    def get(self, request, *args, **kwargs):
        if not self.validate_token(request):
            return Response(
                {
                    "message": (
                        "the password reset token is invalid or has expired."
                    )
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {"message": "the password reset token is valid"},
            status=status.HTTP_200_OK,
        )

    def update(self, request, *args, **kwargs):
        if not self.validate_token(request):
            return Response(
                {
                    "message": (
                        "the password reset token is invalid or has expired."
                    )
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        user = (
            get_user_model()
            .objects.filter(email=serializer.data.get("email"))
            .first()
        )

        if not user:
            return Response(
                {"message": "Email does not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user.set_password(serializer.data.get("new_password"))
        user.save()

        return Response(
            {"message": "Password updated successfully"},
            status=status.HTTP_200_OK,
        )


class EmailResetLinkView(generics.GenericAPIView):
    """
    An endpoint for emailing reset password links.
    """

    serializer_class = EmailSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        email = serializer.data["email"]
        user = get_user_model().objects.filter(email=email).first()

        if not user:
            return Response(
                {"message": "Email does not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        token = PasswordResetTokenGenerator().make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.email))

        reset_url = f"{settings.FRONTEND_URL}/reset/?token={token}&uid={uid}/"

        try:
            send_mail(
                "Elucidate Password Reset",
                f"Your password reset link can be found at: {reset_url}\n"
                + "It will expire in"
                f" {settings.PASSWORD_RESET_TIMEOUT / 60} minutes.",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
        except SMTPAuthenticationError:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        return Response(
            {"message": "Email has been sent"}, status=status.HTTP_200_OK
        )
