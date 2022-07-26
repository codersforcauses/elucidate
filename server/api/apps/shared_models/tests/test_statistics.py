from django.test import TestCase
from django.utils import timezone

from api.apps.shared_models.models.quiz_models import Answer, Question
from api.apps.shared_models.models.statistics_models import (
    QuestionResponse,
)


class QuestionTestCase(TestCase):
    def setUp(self):
        self.creation_time = timezone.now()
        self.q = Question.objects.create(
            text="Question?", question_type=Question.QuestionType.MULTICHOICE
        )
        self.a = Answer.objects.create(
            text="Answer!", question=self.q, is_correct=True
        )
        QuestionResponse.objects.create(
            question=self.q,
            selected_answer=self.a,
        )

    def test(self):
        qr = QuestionResponse.objects.get()

        self.assertIsNone(qr.user)
        self.assertEquals(qr.question, self.q)
        self.assertEquals(qr.selected_answer, self.a)
        self.assertLess(
            (qr.date_submitted - self.creation_time).total_seconds(), 0.1
        )
