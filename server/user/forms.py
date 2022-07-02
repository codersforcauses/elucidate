from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms.fields import EmailField
from django.forms.forms import Form
# from .models import UserDetails


class CreateUserForm(UserCreationForm):
    username = forms.CharField(label='username', min_length=5, max_length=100)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label="password confirmation", widget=forms.PasswordInput)
    first_name = forms.CharField(label='first name')
    last_name = forms.CharField(label='last name')

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

    # class Meta:
    #     model = User
    #     fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']