from django.test import TestCase
from django.utils import timezone
from ..models.quiz_models import Question, Answer
from ..models.statistics_models import QuizStatistics

from datetime import timedelta

MC = Question.QuestionType.MULTICHOICE


class QuestionTestCase(TestCase):
    def setUp(self):
        self.creation_time = timezone.now()
        QuizStatistics.objects.create(
            name="name",
            question_count=3,
            total_marks=3,
            user_mark=2,
            time_taken=timedelta(seconds=5),
        )

    def test(self):
        qr = QuizStatistics.objects.all()[0]

        self.assertIsNone(qr.user)
        self.assertEquals(qr.name, "name")
        self.assertEquals(qr.question_count, 3)
        self.assertEquals(qr.total_marks, 3)
        self.assertEquals(qr.user_mark, 2)
        self.assertEquals(qr.time_taken, timedelta(seconds=5))
        self.assertLess(
            (qr.date_taken - self.creation_time).total_seconds(), 0.1
        )
