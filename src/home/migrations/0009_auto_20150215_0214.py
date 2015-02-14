# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20150215_0210'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together=set([('hall', 'start_time', 'end_time')]),
        ),
    ]
