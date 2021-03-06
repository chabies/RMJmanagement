# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 19:40
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSpecies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockmanagement.ProductCategory')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockmanagement.ProductSpecies'),
        ),
    ]
