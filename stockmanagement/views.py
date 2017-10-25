# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from . import models
from . import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.

def category_list(request):
    categories = models.Category.objects.all()
    return render(request, 'stockmanagement/category_list.html', {'categories':categories})

def subcategory_list(request, pk): #category_detail
    category = get_object_or_404(models.Category, pk=pk)
    return render(request, 'stockmanagement/subcategory_list.html', {'category':category})

def product_profiles(request, category_pk, subcategory_pk): #subcategory
    subcategory = get_object_or_404(models.Subcategory, category_id=category_pk, pk=subcategory_pk)
    return render(request, 'stockmanagement/product_profiles.html', {'subcategory':subcategory})

def add_product(request, category_pk, subcategory_pk):
    form = forms.AddProduct()
    subcategory = get_object_or_404(models.Subcategory, category_id=category_pk, pk=subcategory_pk)

    if request.method == 'POST':
        form = forms.AddProduct(request.POST)
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.subcategory = subcategory
            new_product.save()
            messages.add_message(request, messages.SUCCESS, "New Product Added!")
            return HttpResponseRedirect(subcategory.get_absolute_url())
    return render(request, 'stockmanagement/add_product.html', {'form':form}, {'subcategory':subcategory})
