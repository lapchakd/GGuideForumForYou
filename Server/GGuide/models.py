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
        fields = ('username', 'email')

    def __str__(self):
        return f'{self.username}'


class Userlogin(forms.Form):
    username = forms.CharField(label='username', max_length=10)
    password = forms.CharField(label='password', max_length=22)


class ProfileModel(models.Model):
    img = models.ImageField(default='/profile_images/default.png')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'


class ProfileForm(forms.Form):
        Image = forms.ImageField(help_text="Foto must be 150x150")


