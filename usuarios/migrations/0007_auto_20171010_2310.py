# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 23:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_auto_20171010_2253'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='professor',
            options={'permissions': (('pode_acessar_area_professor', 'pode acessar area professor'), ('disciplina', 'pode fazer o crud de disciplina'))},
        ),
    ]
