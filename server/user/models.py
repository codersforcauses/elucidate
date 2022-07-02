from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserDetails(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    # Change this to be a salted password hash
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Check to see how this works
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
