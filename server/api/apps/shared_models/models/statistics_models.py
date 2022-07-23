from django.conf import settings
from django.db import models
from .quiz_models import Question, Answer

from datetime import timedelta


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
