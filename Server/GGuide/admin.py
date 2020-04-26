from django.contrib import admin

from .models import Article, ProfileModel, CommentsModel

# Register your models here.
admin.site.register(Article)
admin.site.register(ProfileModel)
admin.site.register(CommentsModel)

