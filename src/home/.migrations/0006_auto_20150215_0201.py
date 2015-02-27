# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20150215_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
