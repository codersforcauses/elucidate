from django.db import models
from django.contrib.auth.models import User
from . import defines


class Quiz_Question(models.Model):
    question_type = models.PositiveIntegerField(null=True)
    question = models.CharField(max_length=defines.QUIZ_QUESTION_MAXLEN)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f"question: {self.question}, type: {self.question_type}"


class Question_Answer(models.Model):
    question = models.ForeignKey(Quiz_Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField()
    answer = models.CharField(max_length=defines.QUIZ_ANSWER_MAXLEN)
    
    def __str__(self):
        return f"answer: {self.answer}, is correct: {self.is_correct}"


class Question_Tag(models.Model):
    question = models.ManyToManyField(Quiz_Question)
    tag = models.CharField(max_length=defines.QUIZ_TAG_MAXLEN)
    
    def __str__(self):
        return self.tag