# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-29 16:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resultados', '0004_remove_resultado_alunos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Resultado',
            new_name='Resultados',
        ),
    ]
