from django.db import models
from . import defines


class Quiz(models.Model):
    name = models.CharField(max_length=defines.QUIZ_NAME_MAXLEN)
    subject = models.CharField(max_length=defines.QUIZ_SUBJECT_MAXLEN)
    time_limit = models.DurationField()
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
    text = models.TextField(blank=True, null=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.CharField(max_length=defines.ANSWER_TEXT_MAXLEN)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text

