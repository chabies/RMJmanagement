# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category, Subcategory, Product
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

class ProductAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Product, ProductAdmin)
