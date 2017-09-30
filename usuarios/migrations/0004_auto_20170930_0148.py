# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 01:48
from __future__ import unicode_literals

from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20170927_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='img',
            field=models.ImageField(blank=True, upload_to='img/original/'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='thumb',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='img/thumb/'),
        ),
    ]
