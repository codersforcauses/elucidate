from django.db import models
from django.utils.translation import gettext_lazy as _
from . import defines

from datetime import timedelta


class Quiz(models.Model):
    name = models.CharField(max_length=defines.QUIZ_NAME_MAXLEN)
    subject = models.CharField(max_length=defines.QUIZ_SUBJECT_MAXLEN)
    time_limit = models.DurationField(default=timedelta(minutes=5))
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name


class Objective(models.Model):
    name = models.CharField(max_length=defines.OBJECTIVE_NAME_MAXLEN)
    quiz = models.ManyToManyField(Quiz)
    
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=defines.TAG_NAME_MAXLEN)
    quiz = models.ManyToManyField(Quiz)
    
    def __str__(self):
        return self.name


class Question(models.Model):

    class QuestionType(models.TextChoices):
        MULTICHOICE = "MC", _("Multiple Choice")
        SHORT_ANSWER = "SA", _("Short Answer")


    text = models.TextField(blank=True, default="")
    question_type = models.CharField(max_length=2,
                                     choices=QuestionType.choices,
                                     default=QuestionType.MULTICHOICE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.CharField(max_length=defines.ANSWER_TEXT_MAXLEN)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text

