# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20150215_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.EmailField(max_length=50, verbose_name=b'Email'),
            preserve_default=True,
        ),
    ]
