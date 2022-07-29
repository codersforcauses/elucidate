from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from api.apps.shared_models.models import statistics_models
# Create your tests here.

class UserStatisticsTest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            "test@gamil.com",
            "password",
            grade = "50",
            first_name = "Sam",
            last_name = "Sean"
        )
        self.client.login(email="test@gamil.com", password="password")
        US = statistics_models.UserStatistics.objects.create(user = self.user)
        
    def test_user_statistics(self):
        US = statistics_models.UserStatistics.objects.get(first_name = "Sam")
        response = self.client.get(
            reverse("user_statistics:fish",kwargs={"user_pk": US.pk})
        )
        print(response.data)