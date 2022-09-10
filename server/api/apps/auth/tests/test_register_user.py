from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class RegisterTestCase(APITestCase):
    def test_get_request(self):
        """
        GIVEN: GET request to endpoint '/api/auth/register'
        THEN: The API HTTP Response Code should be 405
        """
        url = reverse("register")

        expected_response = {"detail": 'Method "GET" not allowed.'}
        response = self.client.get(url)
        self.assertEqual(
            response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED
        )
        self.assertDictEqual(expected_response, response.json())

    def test_valid(self):
        """
        GIVEN: The endpoint '/api/auth/register'
        THEN: The API HTTP Response Code should be 201
        """
        url = reverse("register")
        body = {
            "email": "john.doe@example.com",
            "grade": "Grade 11",
            "first_name": "John",
            "last_name": "Doe",
            "password": "password",
        }

        # will also return id
        expected_response = {
            "email": "john.doe@example.com",
            "grade": "Grade 11",
            "first_name": "John",
            "last_name": "Doe",
        }

        response = self.client.post(url, body, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertDictContainsSubset(expected_response, response.json())

    def test_no_fields(self):
        """
        GIVEN: The endpoint '/api/auth/register' and no fields
        THEN: The API HTTP Response Code should be 400
        """
        url = reverse("register")
        body = {
            "email": "",
            "password": "",
            "grade": "",
            "first_name": "",
            "last_name": "",
        }

        expected_response = {
            "email": ["This field may not be blank."],
            "first_name": ["This field may not be blank."],
            "grade": ["This field may not be blank."],
            "last_name": ["This field may not be blank."],
            "password": ["This field may not be blank."],
        }

        response = self.client.post(url, body, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertDictEqual(expected_response, response.json())

    def test_invalid_fields(self):
        """
        GIVEN: The endpoint '/api/auth/register' and invalid fields
        THEN: The API HTTP Response Code should be 400
        """
        url = reverse("register")
        body = {
            "email": "john.doe",
            "grade": "3",
            "first_name": "John",
            "last_name": "Doe",
            "password": "pass",
        }

        expected_response = {
            "email": ["Enter a valid email address."],
            "password": [
                "This password is too short. It must contain at least 6"
                " characters."
            ],
            "grade": ["The grade should be 'Grade 11', 'Grade 12' or 'Other'"],
        }

        response = self.client.post(url, body, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertDictContainsSubset(expected_response, response.json())
