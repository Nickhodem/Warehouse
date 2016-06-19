# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storehouse', '0008_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productparts',
            field=models.ManyToManyField(blank=True, related_name='_product_productparts_+', to='storehouse.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='wareparts',
            field=models.ManyToManyField(blank=True, to='storehouse.Ware'),
        ),
    ]
