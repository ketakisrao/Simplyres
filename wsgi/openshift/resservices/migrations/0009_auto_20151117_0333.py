# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resservices', '0008_auto_20151117_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.CharField(max_length=20),
        ),
    ]
