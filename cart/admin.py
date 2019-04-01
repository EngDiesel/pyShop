# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import cart


class cartAdmin(admin.ModelAdmin):
    class meta:
        model = cart

admin.site.register(cart, cartAdmin)

