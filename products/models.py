# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class category(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

    def __unicode__(self):
        return u'%s' % self.name


class product(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    category = models.ForeignKey(category, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'%s' % self.name
