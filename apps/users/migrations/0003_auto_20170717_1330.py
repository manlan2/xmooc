# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-07-17 05:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170531_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default=b'image/default.jpg', upload_to=b'image/%Y/%m'),
        ),
    ]