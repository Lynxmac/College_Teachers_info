# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-04 06:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='slug',
            field=models.SlugField(default='', unique=True, verbose_name='\u94fe\u63a5\u522b\u540d'),
            preserve_default=False,
        ),
    ]