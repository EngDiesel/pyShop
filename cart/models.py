# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from products.models import product


from django.db import models

class cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)
    products = models.ManyToManyField(product, null=True, blank=True)

    def __str__(self):
        return self.user.username + "'s Cart"