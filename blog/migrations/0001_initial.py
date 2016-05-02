# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tittle', models.CharField(max_length=20, verbose_name=b'\xe9\xa2\x98\xe7\x9b\xae')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('snippet', models.TextField()),
                ('create_time', models.DateField()),
                ('pub_time', models.DateField()),
                ('update_time', models.DateField()),
                ('is_public', models.BooleanField()),
                ('is_top', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=20, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(to='blog.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
    ]
