# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-29 16:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resultados', '0003_auto_20171029_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultado',
            name='alunos',
        ),
    ]