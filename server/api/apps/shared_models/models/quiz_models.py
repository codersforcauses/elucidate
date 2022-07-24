from django import forms
from django.forms import ValidationError
from django.conf import settings
from django.db import models
from . import defines


class Subject(models.Model):
    name = models.CharField(max_length=defines.TAG_NAME_MAXLEN)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=defines.TAG_NAME_MAXLEN)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

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
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    topics = models.ManyToManyField(Topic, blank=True)

    def __str__(self):
        return self.text


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["subject", "topics"]

    def clean(self):
        subject = self.cleaned_data.get("subject")
        topics = self.cleaned_data.get("topics")
        if subject and topics:
            for topic in topics:
                if topic.subject != subject:
                    raise ValidationError(f"Invalid topic \"{topic}\": this topic belongs to the subject \"{topic.subject}\" whereas the question belongs to the subject \"{subject}\".")
        return self.cleaned_data


class Answer(models.Model):
    text = models.CharField(max_length=defines.ANSWER_TEXT_MAXLEN)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
