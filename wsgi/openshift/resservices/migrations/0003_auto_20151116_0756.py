# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resservices', '0002_auto_20151115_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='googlemaps_id',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='location',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
