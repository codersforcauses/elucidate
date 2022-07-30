from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from api.apps.shared_models.models import statistics_models, quiz_models

# Create your tests here.


class UserStatisticsTest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            "test@gamil.com",
            "password",
            grade="50",
            first_name="Sam",
            last_name="Sean",
        )
        self.client.login(email="test@gamil.com", password="password")
        US = statistics_models.UserStatistics.objects.create(user=self.user)
        QS = statistics_models.QuizStatistics.objects.create(user=self.user, quiz_title="Math Quiz", score=100)
        Q = quiz_models.Question.objects.create(question_type="MC", marks=100, creator=self.user)

    def test_user_statistics(self):
        US = statistics_models.UserStatistics.objects.get(
            user__first_name="Sam"
        )
        response = self.client.get(
            reverse("user_statistics:stats", kwargs={"user_pk": US.user.pk})
        )
        print(response.data)

    def test_quiz_list(self):
        QS = statistics_models.UserStatistics.objects.get(
            user__first_name="Sam"
        )
        response = self.client.get(
            reverse("user_statistics:quiz-list", kwargs={"user_pk": QS.user.pk})
        )
        print(response.data)

    def test_question_list(self):
        Q = statistics_models.UserStatistics.objects.get(
            user__first_name="Sam"
        )
        response = self.client.get(
            reverse("user_statistics:question-list", kwargs={"user_pk": Q.user.pk})
        )
        print(response.data)



