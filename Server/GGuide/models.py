from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils import timezone


class Article(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=128)
    text = models.TextField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    article_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail', args=[self.slug])


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


# class CommentsForm(forms.Form):                                   now isn't using
#     comment = models.CharField(label='text', max_length=250)


class Comments(models.Model):
    user_img = models.ImageField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.SET_NULL)
    text = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.user}'