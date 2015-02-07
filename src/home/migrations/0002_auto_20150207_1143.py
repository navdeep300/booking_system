# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('email', models.EmailField(unique=True, max_length=50)),
                ('event_name', models.CharField(unique=True, max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hall', models.CharField(unique=True, max_length=25)),
                ('seats', models.PositiveSmallIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='BookingStatus',
        ),
        migrations.AddField(
            model_name='booking',
            name='hall',
            field=models.ForeignKey(to='home.Hall'),
            preserve_default=True,
        ),
    ]
