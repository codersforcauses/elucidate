from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase


class AuthTestCase(APITestCase):
    def setUp(self):
        self.testuser = User.objects.create_user(
            'james', 'john@james.com', 'password')
        self.testuser.save()

    def test_get_token(self):
        """
        GIVEN: The endpoint '/api/auth/token' and an active user
        WHEN: An HTTP request is sent in the endpoint with the HTTP body that contains account name and password
        THEN: The API HTTP Response Code should be 201
        AND: The Body should contain pk and jwt token
        """
        url = reverse('get-jwt-token')
        body = {
            'username': 'james',
            'password': 'password'
        }

        response = self.client.post(url, body, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Mints a valid JWT
        assert response.data['token'].startswith('eyJ0')

    def test_get_token_inactive_user(self):
        """
        GIVEN: The endpoint '/api/auth/token' and an inactive user
        WHEN: An HTTP request is sent in the endpoint with the HTTP body that contains account name and password
        THEN: The API HTTP Response Code should be 400
        """
        url = reverse('get-jwt-token')
        self.testuser.is_active = False
        self.testuser.save()

        body = {
            'username': 'test_user',
            'password': 'password'
        }

        response = self.client.post(url, body, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_refresh_token(self):
        """
        GIVEN: The endpoint '/api/auth/token/refresh'
        WHEN: An HTTP request is sent in the endpoint with the HTTP body that contains account name and password
        THEN: The API HTTP Response Code should be 201
        """
        get_token_url = reverse('get-jwt-token')
        get_token_body = {
            'username': 'james',
            'password': 'password'
        }
        get_token_response = self.client.post(
            get_token_url, get_token_body, format='json')

        refresh_token_url = reverse('refresh-jwt-token')
        refresh_token_body = {
            'token': get_token_response.data['token']
        }

        refresh_token_response = self.client.post(
            refresh_token_url, refresh_token_body, format='json')
        self.assertEqual(refresh_token_response.status_code,
                         status.HTTP_201_CREATED)
