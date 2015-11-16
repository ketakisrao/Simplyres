# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('resservices', '0004_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.DateField(default=datetime.date),
        ),
        migrations.AddField(
            model_name='booking',
            name='time',
            field=models.TimeField(default=datetime.time),
        ),
        migrations.AddField(
            model_name='booking',
            name='username',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
