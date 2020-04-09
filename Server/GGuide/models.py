from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Article(models.Model):
    author = models.CharField(max_length=22)
    title = models.CharField(max_length=128)
    text = models.TextField()


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=10)
    email = forms.CharField(max_length=22)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1')