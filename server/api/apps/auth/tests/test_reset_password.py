from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import status
from rest_framework.test import APITestCase


class ResetPasswordTestCase(APITestCase):
    def setUp(self):
        self.testuser = get_user_model().objects.create_user(
            email="john.doe@example.com",
            first_name="John",
            last_name="Doe",
            grade="Grade 11",
            password="password",
        )
        self.testuser.save()

    def test_send_reset_email(self):
        """
        GIVEN: The endpoint '/api/auth/reset/email/' and an active user
        WHEN: A POST request is sent to the endpoint with the HTTP body that
            contains an email address corresponding to a valid account
        THEN: The API HTTP Response Code should be 200
        AND: The SMTP server will be called to send a password reset email to
            the specified address
        """
        url = reverse("send-reset-email")
        body = {"email": "john.doe@example.com"}

        response = self.client.post(url, body, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_verify_reset_token(self):
        """
        WHEN: A GET request is sent to the endpoint with uid and token as url
            parameters
        THEN: Returns 200 status code if the token and uid is valid
        """

        user = (
            get_user_model()
            .objects.filter(email="john.doe@example.com")
            .first()
        )
        token = PasswordResetTokenGenerator().make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.email))

        reset_url = f"{reverse('reset')}?token={token}&uid={uid}/"

        response = self.client.get(reset_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_reset_password(self):
        """
        GIVEN: The endpoint '/api/auth/reset/' and a valid uid and token
        WHEN: A PUT request is sent to the endpoint with uid and token as url
            parameters and password in JSON body
        THEN: Returns 200 status code if the password has been reset.
        """

        user = (
            get_user_model()
            .objects.filter(email="john.doe@example.com")
            .first()
        )
        token = PasswordResetTokenGenerator().make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.email))

        reset_url = f"{reverse('reset')}?token={token}&uid={uid}/"

        body = {"password": "123456"}

        response = self.client.put(reset_url, body, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
