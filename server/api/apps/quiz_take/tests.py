from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.timezone import now
from rest_framework import status
from rest_framework.test import APITestCase

from api.apps.shared_models.models.quiz_models import (
    Answer,
    Question,
    Subject,
    Topic,
)
from api.apps.shared_models.models.statistics_models import (
    QuestionResponse,
    QuizStatistics,
)


class QuizTakeTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            "test@test.com",
            "password",
            grade="12",
            first_name="John",
            last_name="Smith",
        )
        self.client.login(email="test@test.com", password="password")

        s = Subject.objects.create(name="Chemistry Unit 3")
        t = Topic.objects.create(name="Electrochemistry", subject=s)
        q1 = Question.objects.create(
            subject=s,
            question="What is the difference between reduction and oxidation?",
            question_type="MC",
            marks=1,
            creator=self.user,
        )
        q1.topics.add(t)
        Answer.objects.create(
            answer=(
                "Reduction is the gain of an electron, and oxidation the loss"
            ),
            is_correct=True,
            question=q1,
        )
        Answer.objects.create(
            answer=(
                "Reduction is the loss of an electron, and oxidation the gain"
            ),
            is_correct=False,
            question=q1,
        )

    def test_question_detail(self):
        q = Question.objects.get()
        response = self.client.get(
            reverse("quiz_take:question_detail", kwargs={"question_pk": q.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["question"], q.question)
        self.assertEqual(response.data["creator"], q.creator.pk)
        self.assertEqual(len(response.data["topics"]), q.topics.count())

    def test_answers_list(self):
        q = Question.objects.get()
        response = self.client.get(
            reverse("quiz_take:answers_list", kwargs={"question_pk": q.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), Answer.objects.count())

    def test_answer_detail(self):
        q = Question.objects.get()
        a = Answer.objects.get(is_correct=True)
        response = self.client.get(
            reverse(
                "quiz_take:answer_detail",
                kwargs={"question_pk": q.pk, "answer_pk": a.pk},
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["answer"], a.answer)
        self.assertEqual(response.data["question"], a.question.pk)

    def test_topics_list(self):
        q = Question.objects.get()
        response = self.client.get(
            reverse("quiz_take:topics_list", kwargs={"question_pk": q.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), Topic.objects.count())

    def test_topic_detail(self):
        q = Question.objects.get()
        t = Topic.objects.get()
        response = self.client.get(
            reverse(
                "quiz_take:topic_detail",
                kwargs={"question_pk": q.pk, "topic_pk": t.pk},
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], t.name)
        self.assertEqual(response.data["subject"], t.subject.pk)

    def test_subject_detail(self):
        q = Question.objects.get()
        s = Subject.objects.get()
        response = self.client.get(
            reverse("quiz_take:subject_detail", kwargs={"question_pk": q.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], s.name)

    def test_question_response_create(self):
        q = Question.objects.get()
        a = Answer.objects.get(is_correct=True)
        response = self.client.post(
            reverse("quiz_take:question_response_create"),
            {"user": self.user.pk, "question": q.pk, "selected_answer": a.pk},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        qr = QuestionResponse.objects.get()
        self.assertEqual(qr.user, self.user)
        self.assertEqual(qr.question, q)
        self.assertEqual(qr.selected_answer, a)

    def test_quiz_statistics_create(self):
        s = Subject.objects.get()
        t = Topic.objects.get()
        response = self.client.post(
            reverse("quiz_take:quiz_statistics_create"),
            {
                "user": self.user.pk,
                "quiz_title": "Y12S2 Chemistry",
                "subject": s.pk,
                "date_taken": now().date(),
                "topics": [t.pk],
                "score": 85.0,
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        qs = QuizStatistics.objects.get()
        self.assertEqual(qs.user, self.user)
        self.assertEqual(qs.quiz_title, response.data["quiz_title"])
        self.assertEqual(qs.subject, s)
        self.assertEqual(str(qs.date_taken), response.data["date_taken"])
        self.assertEqual(qs.topics.count(), 1)
        self.assertEqual(qs.score, 85.0)
