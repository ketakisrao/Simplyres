# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resservices', '0009_auto_20151117_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='username',
            field=models.CharField(default=b'ketakisrao', max_length=100),
        ),
    ]
