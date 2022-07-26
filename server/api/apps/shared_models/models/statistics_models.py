from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from . import defines
from .quiz_models import Answer, Question, Subject, Topic


def sum_marks(x):
    total = 0
    for i in x:
        if i.question and i.question.marks:
            total += i.question.marks
    return total


class QuestionResponse(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.ForeignKey(
        Answer, on_delete=models.CASCADE, null=True
    )
    date_submitted = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str((self.question, self.selected_answer))


class UserStatistics(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False
    )

    class Meta:
        verbose_name_plural = "User statistics"

    @property
    def questions_created(self):
        return Question.objects.filter(creator=self.user).count()

    @property
    def average_score(self):
        total = sum_marks(QuestionResponse.objects.filter(user=self.user))
        if total == 0:
            return None
        return (
            sum_marks(
                QuestionResponse.objects.filter(
                    user=self.user, selected_answer__is_correct=True
                )
            )
            / total
        )

    @property
    def quizzes_completed(self):
        return QuizStatistics.objects.filter(user=self.user).count()

    def __str__(self):
        return str(self.user)


class QuizStatistics(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False
    )
    quiz_title = models.CharField(max_length=defines.QUIZ_NAME_MAXLEN)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    topics = models.ManyToManyField(Topic, blank=True)
    date_taken = models.DateField(null=True)
    score = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)]
    )

    class Meta:
        constraints = (
            models.CheckConstraint(
                check=models.Q(score__gte=0.0) & models.Q(score__lte=100.0),
                name="QuizStatistics_score_range",
            ),
        )
        verbose_name_plural = "Quiz statistics"

    def __str__(self):
        return str((self.user, self.quiz_title))


class QuestionStatistics(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, null=False
    )

    class Meta:
        verbose_name_plural = "Question statistics"

    @property
    def number_attempts(self):
        return QuestionResponse.objects.filter(question=self.question).count()

    @property
    def average_score(self):
        total = sum_marks(
            QuestionResponse.objects.filter(question=self.question)
        )
        if total == 0:
            return None
        return (
            sum_marks(
                QuestionResponse.objects.filter(
                    question=self.question, selected_answer__is_correct=True
                )
            )
            / total
        )

    def __str__(self):
        return str(self.question)


class TopicStatistics(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = "Topic statistics"

    @property
    def average_score(self):
        total = sum_marks(
            QuestionResponse.objects.filter(question__topics__in=[self.topic])
        )
        if total == 0:
            return None
        return (
            sum_marks(
                QuestionResponse.objects.filter(
                    question__topics__in=[self.topic],
                    selected_answer__is_correct=True,
                )
            )
            / total
        )
