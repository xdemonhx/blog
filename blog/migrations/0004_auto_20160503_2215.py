# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160502_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tittle',
            field=models.CharField(max_length=40, verbose_name=b'\xe9\xa2\x98\xe7\x9b\xae'),
        ),
    ]
