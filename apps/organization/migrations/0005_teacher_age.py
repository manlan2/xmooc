# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-11 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20170606_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='age',
            field=models.IntegerField(default=18, verbose_name='\u5e74\u9f84'),
        ),
    ]
