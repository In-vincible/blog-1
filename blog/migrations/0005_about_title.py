# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='title',
            field=models.CharField(max_length=20, default='About me', verbose_name='title'),
            preserve_default=True,
        ),
    ]
