# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160503_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='access_count',
            field=models.IntegerField(default=0, verbose_name=b'\xe7\x82\xb9\xe5\x87\xbb\xe9\x87\x8f'),
        ),
    ]
