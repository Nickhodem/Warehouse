# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storehouse', '0002_auto_20160617_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='ware',
            name='provider_name',
            field=models.CharField(default=b'dostawca', max_length=1000),
        ),
        migrations.AddField(
            model_name='ware',
            name='provider_url',
            field=models.URLField(blank=True),
        ),
    ]
