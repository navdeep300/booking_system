# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20150216_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(default=datetime.date.today),
            preserve_default=True,
        ),
    ]
