# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resservices', '0007_booking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='booking',
            name='username',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='googlemaps_id',
            field=models.CharField(max_length=100),
        ),
    ]
