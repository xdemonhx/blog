from django.contrib import admin
from blog.models import Category,Article
# Register your models here.

admin.sites.site.register(Category)
admin.sites.site.register(Article)
