# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storehouse', '0013_auto_20160622_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ware',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
