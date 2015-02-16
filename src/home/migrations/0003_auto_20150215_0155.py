# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20150207_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.EmailField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='booking',
            name='event_name',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
