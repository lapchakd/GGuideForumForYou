from django.db import models
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
    article_image = models.ImageField(upload_to='article_images', blank=True)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')

    def get_like_url(self):
        return reverse("like-toggle", args=[self.slug])

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def snippet(self):
        return self.text[:120] + '...'
    
    def get_absolute_url(self):
        return reverse('detail', args=[self.slug])


class ProfileModel(models.Model):
    img = models.ImageField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField(User, related_name='friends')

    def __str__(self):
        return f'{self.user}'


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=250)
    comments_date = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, blank=True, related_name='comment_likes')

    def __str__(self):
        return f'{self.user}/{self.article}'