# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.conf import settings
from products.models import category, product
from django.shortcuts import render
from cart.models import cart

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def checkout(request):
    publishkey = settings.STRIPE_PUBLISHABLE_KEY
    customer_id = request.user.userstripe.stripe_id
    amount = 0
    curr_cart = cart.objects.get(user=request.user)
    curr_products = curr_cart.products.all()
    for item in curr_products:
        amount += item.price 


    categories = category.objects.all()

    if request.method == 'POST':
        token = request.POST['stripeToken']
        try:
            customer = stripe.Customer.retrieve(customer_id)
            customer.sources.create(source=token)
            amount *= 100
            
            charge = stripe.Charge.create(
                amount=amount,
                currency='EGP',
                description='Example charge',
                customer=customer,
            )
            amount /= 100

        except stripe.error.CardError as e:
            print(e.message)        
        print(token)
    template = 'checkout.html'
    context = {'publishkey': publishkey, 'amount': amount, 'categories': categories }
    return render(request, template, context)
