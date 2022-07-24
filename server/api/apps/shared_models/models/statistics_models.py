from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from .quiz_models import Question, Answer

from datetime import timedelta
from . import defines


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
    quizzes_completed = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "User statistics"

    @property
    def questions_created(self):
        return Question.objects.filter(creator=self.user).count()

    @property
    def average_score(self):
        return QuestionResponse.objects.filter(user=self.user, selected_answer__is_correct=True).count() / QuestionResponse.objects.filter(user=self.user).count()

    def __str__(self):
        return str(self.user)


class QuizStatistics(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False
    )
    quiz_title = models.CharField(max_length=defines.QUIZ_NAME_MAXLEN)
    date_taken = models.DateField(null=True)
    score = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])

    class Meta:
        constraints = (
            models.CheckConstraint(
                check=models.Q(score__gte=0.0) & models.Q(score__lte=100.0),
                name="QuizStatistics_score_range"
            ),
        )
        verbose_name_plural = "Quiz statistics"

    def __str__(self):
        return str((self.user, self.quiz_title))


class QuizTag(models.Model):
    name = models.CharField(max_length=defines.TAG_NAME_MAXLEN)
    quiz_statistics = models.ManyToManyField(QuizStatistics)

    def __str__(self):
        return self.name
