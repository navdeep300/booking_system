# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20150221_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='event_name',
            field=models.CharField(unique=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together=set([('hall', 'start_time', 'end_time')]),
        ),
    ]
