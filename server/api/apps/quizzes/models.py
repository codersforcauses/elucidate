from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Quiz(models.Model):

    CATEGORY_CHOICES = (
        ("General", "General"),
        ("Science", "Science"),
        ("Maths", "Maths"),
        ("History", "History"),
        ("Geography", "Geography"),
        ("Art", "Art"),
        ("Literature", "Literature"),
        ("Computer Science", "Computer Science"),
        ("Business", "Business"),
        ("Engineering", "Engineering"),
        ("Medicine", "Medicine"),
    )

    title = models.CharField(max_length=100)
    question = models.CharField(unique=True, max_length=200)
    answer = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(
        max_length=100, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0][0]
    )
    attempts = models.IntegerField(default=0)
    correct = models.IntegerField(default=0)

    def __str__(self):
        return self.title
