# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmanagement', '0006_product_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='longitude',
            field=models.FloatField(default=0),
        ),
    ]
