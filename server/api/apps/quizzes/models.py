from django.contrib.auth import get_user_model
from django.db import models
from api.apps.shared_models.models import quiz_models

User = get_user_model()


class Quiz(models.Model):
    questions = models.ManyToManyField(
        quiz_models.Question, through="QuizQuestion"
    )
    topics = models.ManyToManyField(
        quiz_models.Topic,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    attempts = models.IntegerField(default=0)
    correct = models.IntegerField(default=0)

    def __str__(self):
        return str(self.pk)


# Many to many field
class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(
        quiz_models.Question, on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ("quiz", "question")

    def __str__(self):
        return str(self.pk)
