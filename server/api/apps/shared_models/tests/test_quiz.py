from api.apps.shared_models.models.quiz_models import (
    Answer,
    Question,
    Subject,
    Topic,
)
from django.test import TestCase
from django.utils import timezone


class QuestionTestCase(TestCase):
    def setUp(self):
        self.creation_time = timezone.now()

        Question.objects.create(
            text="Test multiple choice question",
            question_type=Question.QuestionType.MULTICHOICE,
        )
        Question.objects.create(
            text="Test numerical answer question",
            question_type=Question.QuestionType.NUMERIC,
        )
        Question.objects.create(
            text="Test short answer question",
            question_type=Question.QuestionType.SHORT_ANSWER,
        )

    def test_text(self):
        mc = Question.objects.get(text="Test multiple choice question")
        self.assertEqual(str(mc), "Test multiple choice question")

        na = Question.objects.get(text="Test numerical answer question")
        self.assertEqual(str(na), "Test numerical answer question")

        sa = Question.objects.get(text="Test short answer question")
        self.assertEqual(str(sa), "Test short answer question")

    def test_question_type(self):
        mc = Question.objects.get(text="Test multiple choice question")
        self.assertEqual(mc.question_type, "MC")

        na = Question.objects.get(text="Test numerical answer question")
        self.assertEqual(na.question_type, "NA")

        sa = Question.objects.get(text="Test short answer question")
        self.assertEqual(sa.question_type, "SA")

    def test_creator(self):
        questions = Question.objects.all()
        for q in questions:
            self.assertIsNone(q.creator)

    def test_date_created(self):
        q = Question.objects.get(text="Test multiple choice question")
        self.assertLess(
            (q.date_created - self.creation_time).total_seconds(), 0.1
        )


class SubjectTestCase(TestCase):
    def setUp(self):
        s = Subject.objects.create(name="Unit 3 Physics")
        Question.objects.create(
            text="This is a physics question",
            question_type=Question.QuestionType.NUMERIC,
            subject=s,
        )

    def test(self):
        q = Question.objects.get(text="This is a physics question")
        s = Subject.objects.get(name="Unit 3 Physics")
        self.assertEqual(str(s), "Unit 3 Physics")
        self.assertEqual(q.subject, s)


class TopicTestCase(TestCase):
    def setUp(self):
        s = Subject.objects.create(name="Unit 3 Physics")
        t = Topic.objects.create(name="Projectile Motion", subject=s)
        q = Question.objects.create(
            text="Another physics question!",
            question_type=Question.QuestionType.SHORT_ANSWER,
            subject=s,
        )
        q.topics.add(t)

    def test(self):
        q = Question.objects.get(text="Another physics question!")
        s = Subject.objects.get(name="Unit 3 Physics")
        t = Topic.objects.get(name="Projectile Motion")
        self.assertEqual(t.subject, s)
        self.assertTrue(t in q.topics.all())


class AnswerTestCase(TestCase):
    def setUp(self):
        q = Question.objects.create(
            text="Question?", question_type=Question.QuestionType.SHORT_ANSWER
        )
        Answer.objects.create(text="Answer!", question=q, is_correct=True)

    def test(self):
        q = Question.objects.get(text="Question?")
        a = Answer.objects.get(text="Answer!")
        self.assertEquals(str(a), "Answer!")
        self.assertEquals(a.text, "Answer!")

        self.assertTrue(a.is_correct)

        self.assertEquals(a.question, q)
