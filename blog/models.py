# -*- coding: utf-8 -*-
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager


# Create your models here.
class Tag(TaggableManager):

    def __unicode__(self):
        return self.name

class Category(models.Model):
    category = models.CharField(max_length=20, verbose_name='分类')
    slug = models.CharField(max_length=20, )

    def __unicode__(self):
        return self.category

    def get_num(self):
        return Article.objects.filter(category__slug__in=[self.slug]).count()



class Article(models.Model):
    category = models.ForeignKey(Category)
    tittle = models.CharField(max_length=20, verbose_name='题目')
    content = RichTextUploadingField()
    snippet = models.TextField()

    create_time = models.DateTimeField()
    pub_time = models.DateTimeField()
    update_time = models.DateTimeField()

    is_public = models.BooleanField()
    is_top = models.BooleanField()

    tag = TaggableManager()

    def __unicode__(self):
        return self.tittle

    def get_tag(self):
        return self.tag.names()

    #def sa