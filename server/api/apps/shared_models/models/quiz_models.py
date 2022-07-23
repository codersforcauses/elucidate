from operator import mod
from django.conf import settings
from django.db import models
from . import defines


class Question(models.Model):
    class QuestionType(models.TextChoices):
        MULTICHOICE = "MC", "Multiple Choice"
        NUMERIC = "NA", "Numerical Answer"
        SHORT_ANSWER = "SA", "Short Answer"

    text = models.TextField(blank=True, default="")
    question_type = models.CharField(
        max_length=2,
        choices=QuestionType.choices,
        default=QuestionType.MULTICHOICE,
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    is_verified = models.BooleanField(default=False)
    mark = models.PositiveIntegerField()

    def __str__(self):
        return self.text


class Subject(models.Model):
    name = models.CharField(max_length=defines.TAG_NAME_MAXLEN)
    question = models.ManyToManyField(Question)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=defines.TAG_NAME_MAXLEN)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Answer(models.Model):
    text = models.CharField(max_length=defines.ANSWER_TEXT_MAXLEN)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
