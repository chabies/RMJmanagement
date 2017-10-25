# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.core.urlresolvers import reverse


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order',]

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stockmanagement:product_profiles', kwargs={
            'category_pk':self.category_id,
            'subcategory_pk':self.id
        })

class Product(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    weight = models.FloatField(max_length=100, default=0)
    stock = models.FloatField(max_length=100)
    order = models.IntegerField(default=0)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    location = models.PointField(srid=4326)
    objects = models.GeoManager()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.location = Point(self.longitude, self.latitude)
        super(Product, self).save(*args, **kwargs)