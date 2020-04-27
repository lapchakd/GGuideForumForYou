from django.contrib import admin


from .models import Article, ProfileModel,Comments

# Register your models here.
admin.site.register(Article)
admin.site.register(ProfileModel)
admin.site.register(Comments)




