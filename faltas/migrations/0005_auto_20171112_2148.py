# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-12 21:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faltas', '0004_auto_20171112_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='falta',
            name='date',
            field=models.DateField(),
        ),
    ]
