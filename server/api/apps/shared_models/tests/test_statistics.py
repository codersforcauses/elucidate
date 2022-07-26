from django.test import TestCase
from django.utils import timezone
from api.apps.shared_models.models.quiz_models import Question, Answer
from api.apps.shared_models.models.statistics_models import QuestionResponse

from datetime import timedelta


class QuestionTestCase(TestCase):
    def setUp(self):
        self.creation_time = timezone.now()
        q = Question.objects.create(text="Question?", question_type=Question.QuestionType.MULTICHOICE)
        a = Answer.objects.create(text="Answer!", question=q, is_correct=True)
        QuestionResponse.objects.create(
            question=q,
            selected_answer=a,
        )

    def test(self):
        q = Question.objects.get(text="Question?")
        a = Answer.objects.get(text="Answer!")
        qr = QuestionResponse.objects.all()[0]

        self.assertEquals(str(qr), str((q, a)))
        self.assertIsNone(qr.user)
        self.assertEquals(qr.question, q)
        self.assertEquals(qr.selected_answer, a)
        self.assertLess(
            (qr.date_submitted - self.creation_time).total_seconds(), 0.1
        )
