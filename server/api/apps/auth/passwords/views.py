from django.shortcuts import render
from base64 import urlsafe_b64encode
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from .serializers import ChangePasswordSerializer
from . import serializers
from rest_framework.permissions import IsAuthenticated 
from api.apps.users.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse 
from django.core.mail import send_mail

# Create your views here.
class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }
            
            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PasswordReset(generics.GenericAPIView):

    serializer_class = serializers.EmailSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data["email"]
        user = User.objects.filter(email = email).first()

        if user:
            token = PasswordResetTokenGenerator().make_token(user)
            reset_url = reverse("reset-password", kwargs={"token": token})
            reset_url = f"localhost:8080{reset_url}"

            send_mail(
                'Elucidate Password Reset',
                f"Your password reset link can be found at: {reset_url}",
                "elucidateautobot@gmail.com",
                [f"{email}"],
                fail_silently = False 
            )

            return Response(
                {
                "message":
                f"Email has been sent"
                },

            status = status.HTTP_200_OK)

        else: Response(
            {
                "message":
                "User does note exist"
            }, status = status.HTTP_400_BAD_REQUEST
        )
