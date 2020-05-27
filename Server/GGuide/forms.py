from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ArticleForm(forms.Form):
    article_image = forms.ImageField(label='article_image')
    header = forms.CharField(label='header', max_length=100)
    text = forms.CharField(label='text', max_length=350)


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=10)
    email = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('username', 'email')

    def __str__(self):
        return f'{self.username}'


class Userlogin(forms.Form):
    username = forms.CharField(label='username', max_length=10)
    password = forms.CharField(label='password', max_length=22)


class ProfileForm(forms.Form):
    Image = forms.ImageField()


class FriendForm(forms.Form):
    username = forms.CharField(label='username', max_length=10)
    email = forms.CharField(label='email', max_length=22)


class CommentsForm(forms.Form):
    comment = forms.CharField(label='comment', max_length=250)

