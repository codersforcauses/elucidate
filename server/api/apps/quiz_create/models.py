from django.db import models
from django.contrib.auth.models import User
from . import defines


class Quiz_Details(models.Model):
    name = models.CharField(max_length=defines.QUIZ_NAME_MAXLEN)
    time_limit = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    number_of_questions = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        qname = self.name
        num = self.number_of_questions
        time = self.time_limit
        return f"name: {qname}, question count: {num}, time limit: {time}"


class Quiz_Question(models.Model):
    quiz = models.ForeignKey(Quiz_Details, on_delete=models.CASCADE)
    is_multichoice = models.BooleanField()
    question = models.CharField(max_length=defines.QUIZ_QUESTION_MAXLEN)
    
    def __str__(self):
        return f"question: {self.question}, multichoice: {self.is_multichoice}"


class Question_Answer(models.Model):
    question = models.ForeignKey(Quiz_Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField()
    answer = models.CharField(max_length=defines.QUIZ_ANSWER_MAXLEN)
    
    def __str__(self):
        return f"answer: {self.answer}, is correct: {self.is_correct}"


class Quiz_Tag(models.Model):
    quiz_details = models.ManyToManyField(Quiz_Details)
    tag = models.CharField(max_length=defines.QUIZ_TAG_MAXLEN)
    
    def __str__(self):
        return self.tag


class Quiz_Objective(models.Model):
    quiz_details = models.ManyToManyField(Quiz_Details)
    objective = models.CharField(max_length=defines.QUIZ_OBJECTIVE_MAXLEN)

    def __str__(self):
        return self.objective