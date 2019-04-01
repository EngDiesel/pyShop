# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import category, product


class categoryAdmin(admin.ModelAdmin):
    class meta:
        model = category

admin.site.register(category, categoryAdmin)


class productAdmin(admin.ModelAdmin):
    class meta:
        model = product

admin.site.register(product, productAdmin)