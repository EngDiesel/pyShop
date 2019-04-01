# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import cart
from products.models import category, product
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect


@login_required
def showCart(request):
    template = 'cart.html'
    user = request.user
    curr_cart, created = cart.objects.get_or_create(user=user)
    cart_products = curr_cart.products.all()
    categories = category.objects.all()
    title = 'Your Cart'
    total = 0
    for item in cart_products:
      total += item.price
    
    context = {
        'title': title,
        'cart_products': cart_products,
        'cart': curr_cart,
        'categories': categories,
        'total': total
      }

    return render(request, template, context)

@login_required
def deleteFromCart(request, product_id):
  curr_cart, created = cart.objects.get_or_create(user=request.user)
  curr_product = product.objects.get(pk=product_id)

  curr_cart.products.remove(curr_product)
  return redirect('/cart/')
