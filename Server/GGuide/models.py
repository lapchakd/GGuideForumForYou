from django.db import models


class Article(models.Model):
    author = models.CharField(max_length=22)
    title = models.CharField(max_length=128)
    text = models.TextField()