# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.conf import settings
from .models import category, product
from cart.models import cart
from django.contrib.auth.decorators import login_required


def allcategories(request):
    categories = category.objects.all()
    title = 'All Categories'
    template = 'categories.html'
    context = {'title': title, 'categories': categories}

    return render(request, template, context)


def categoryFunc(request, category_id):
    categories = category.objects.all()
    curr_category = category.objects.get(pk=category_id)

    products = product.objects.filter(category=curr_category)

    title = curr_category.name + " Products"
    context = {'title': title, 'category': curr_category, 'products': products, 'categories': categories}
    template = 'category.html'

    return render(request, template, context)

@login_required
def addToCart(request, category_id, product_id):
    categories = category.objects.all()
    curr_cart, created = cart.objects.get_or_create(user=request.user)

    curr_product = product.objects.filter(pk=product_id)

    curr_cart.products.add(curr_product.first())

    return redirect('/cart/')


