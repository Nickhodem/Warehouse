# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-18 18:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storehouse', '0009_auto_20160617_2334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('status_open', models.BooleanField(default=False)),
                ('client', models.CharField(max_length=50)),
                ('notes', models.CharField(max_length=1000)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storehouse.Product')),
            ],
        ),
    ]
