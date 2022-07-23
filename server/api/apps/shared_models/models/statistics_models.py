from django.conf import settings
from django.db import models
from .quiz_models import Subject, Topic
from . import defines
from datetime import timedelta


class QuizStatistics(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    name = models.CharField(max_length=defines.QUIZ_NAME_MAXLEN)
    question_count = models.PositiveIntegerField()
    total_marks = models.PositiveIntegerField()
    user_mark = models.PositiveIntegerField()
    subjects = models.ManyToManyField(Subject)
    topics = models.ManyToManyField(Topic)
    time_taken = models.DurationField(default=timedelta())
    date_taken = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str((self.question, self.selected_answer))
