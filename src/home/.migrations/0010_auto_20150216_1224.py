# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20150215_0214'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together=set([('hall', 'date', 'start_time', 'end_time')]),
        ),
    ]
