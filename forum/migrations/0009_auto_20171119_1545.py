# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-19 15:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_auto_20171119_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
