# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 21:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questoes', '0002_questao_enunciado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questao',
            old_name='obervacao',
            new_name='observacao',
        ),
    ]
