from django.test import TestCase
from django.utils import timezone

from api.apps.shared_models.models.quiz_models import (
    Answer,
    Question,
    Subject,
    Topic,
)


class QuestionTestCase(TestCase):
    def setUp(self):
        self.creation_time = timezone.now()

        Question.objects.create(
            question="Test multiple choice question",
            question_type=Question.QuestionType.MULTICHOICE,
        )
        Question.objects.create(
            question="Test numerical answer question",
            question_type=Question.QuestionType.NUMERIC,
        )
        Question.objects.create(
            question="Test short answer question",
            question_type=Question.QuestionType.SHORT_ANSWER,
        )

    def test_question(self):
        mc = Question.objects.get(question="Test multiple choice question")
        self.assertEqual(str(mc), "Test multiple choice question")

        na = Question.objects.get(question="Test numerical answer question")
        self.assertEqual(str(na), "Test numerical answer question")

        sa = Question.objects.get(question="Test short answer question")
        self.assertEqual(str(sa), "Test short answer question")

    def test_question_type(self):
        mc = Question.objects.get(question="Test multiple choice question")
        self.assertEqual(mc.question_type, "MC")

        na = Question.objects.get(question="Test numerical answer question")
        self.assertEqual(na.question_type, "NA")

        sa = Question.objects.get(question="Test short answer question")
        self.assertEqual(sa.question_type, "SA")

    def test_creator(self):
        questions = Question.objects.all()
        for q in questions:
            self.assertIsNone(q.creator)

    def test_date_created(self):
        q = Question.objects.get(question="Test multiple choice question")
        self.assertLess(
            (q.date_created - self.creation_time).total_seconds(), 0.1
        )


class SubjectTestCase(TestCase):
    def setUp(self):
        s = Subject.objects.create(name="Unit 3 Physics")
        Question.objects.create(
            question="This is a physics question",
            question_type=Question.QuestionType.NUMERIC,
            subject=s,
        )

    def test(self):
        q = Question.objects.get(question="This is a physics question")
        s = Subject.objects.get(name="Unit 3 Physics")
        self.assertEqual(str(s), "Unit 3 Physics")
        self.assertEqual(q.subject, s)


class TopicTestCase(TestCase):
    def setUp(self):
        s = Subject.objects.create(name="Unit 3 Physics")
        t = Topic.objects.create(name="Projectile Motion", subject=s)
        q = Question.objects.create(
            question="Another physics question!",
            question_type=Question.QuestionType.SHORT_ANSWER,
            subject=s,
        )
        q.topics.add(t)

    def test(self):
        q = Question.objects.get(question="Another physics question!")
        s = Subject.objects.get(name="Unit 3 Physics")
        t = Topic.objects.get(name="Projectile Motion")
        self.assertEqual(t.subject, s)
        self.assertTrue(t in q.topics.all())


class AnswerTestCase(TestCase):
    def setUp(self):
        q = Question.objects.create(
            question="Question?",
            question_type=Question.QuestionType.SHORT_ANSWER,
        )
        Answer.objects.create(answer="Answer!", question=q, is_correct=True)

    def test(self):
        q = Question.objects.get(question="Question?")
        a = Answer.objects.get(answer="Answer!")
        self.assertEquals(str(a), "Answer!")
        self.assertEquals(a.answer, "Answer!")

        self.assertTrue(a.is_correct)

        self.assertEquals(a.question, q)
