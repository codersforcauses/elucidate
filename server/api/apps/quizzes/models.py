from django.contrib.auth import get_user_model
from django.db import models
from api.apps.shared_models.models import quiz_models

User = get_user_model()


class Quiz(models.Model):
    topic = models.ManyToManyField(
        quiz_models.Topic,
    )
    questions = models.ManyToManyField(
        quiz_models.Question,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    attempts = models.IntegerField(default=0)
    correct = models.IntegerField(default=0)

    def __str__(self):
        return str(self.pk)
