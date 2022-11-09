from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase

from api.apps.shared_models.models.quiz_models import Question, Subject, Topic


class QuizGenerateTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            "test@test.com",
            "password",
            grade="12",
            first_name="John",
            last_name="Smith",
        )
        self.client.login(email="test@test.com", password="password")

        self.s = Subject.objects.create(name="Chemistry Unit 3")
        self.s2 = Subject.objects.create(name="Chemistry Unit 4")
        self.t = Topic.objects.create(name="Electrochemistry", subject=self.s)
        self.t2 = Topic.objects.create(name="Biochemistry", subject=self.s2)
        self.q1 = Question.objects.create(
            subject=self.s,
            text="What is the difference between reduction and oxidation?",
            question_type="MC",
            marks=1,
            creator=self.user,
            is_verified=True,
        )
        self.q1.topics.add(self.t)
        self.q2 = Question.objects.create(
            subject=self.s2,
            text="2",
            question_type="MC",
            marks=1,
            creator=self.user,
            is_verified=True,
        )
        self.q2.topics.add(self.t2)

    def test_question_generation(self):
        response = self.client.post(
            reverse("quiz_generate:generate-quiz"),
            {"subject": self.s.pk, "topics": [self.t.pk], "question_count": 1},
            format="json",
        )
        self.assertEqual(response.data["pk_array"], [self.q1.pk])

        response = self.client.post(
            reverse("quiz_generate:generate-quiz"),
            {
                "subject": self.s2.pk,
                "topics": [self.t2.pk],
                "question_count": 1,
            },
            format="json",
        )
        self.assertEqual(response.data["pk_array"], [self.q2.pk])

    def test_subject_exists(self):
        response = self.client.post(
            reverse("quiz_generate:subject-exists"),
            {"name": self.s.name},
            format="json",
        )
        self.assertEqual(response.data["pk"], self.s.pk)

    def test_topic_exists(self):
        response = self.client.post(
            reverse("quiz_generate:topic-exists"),
            {"subject": self.s2.pk, "name": self.t2.name},
            format="json",
        )
        self.assertEqual(response.data["pk"], self.t2.pk)
