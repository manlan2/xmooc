# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-18 04:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_course_course_org'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='\u89c6\u9891\u5730\u5740'),
        ),
    ]
