from django.db import models
from django.utils.translation import gettext_lazy as _
from . import defines


class Question(models.Model):
    class QuestionType(models.TextChoices):
        MULTICHOICE = "MC", _("Multiple Choice")
        SHORT_ANSWER = "SA", _("Short Answer")


    text = models.TextField(blank=True, default="")
    question_type = models.CharField(max_length=2,
                                     choices=QuestionType.choices,
                                     default=QuestionType.MULTICHOICE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.text


class Tag(models.Model):
    name = models.CharField(max_length=defines.TAG_NAME_MAXLEN)
    question = models.ManyToManyField(Question)
    
    def __str__(self):
        return self.name


class Answer(models.Model):
    text = models.CharField(max_length=defines.ANSWER_TEXT_MAXLEN)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text

