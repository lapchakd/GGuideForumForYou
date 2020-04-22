from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class Article(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
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
    img = models.ImageField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField(User, related_name='friend')

    def __str__(self):
        return f'{self.user}'


class ProfileForm(forms.Form):
    Image = forms.ImageField()


class FriendForm(forms.Form):
    username = forms.CharField(label='username', max_length=10)
    email = forms.CharField(label='email', max_length=22)


