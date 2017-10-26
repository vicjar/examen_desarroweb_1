# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from decimal import Decimal
# Create your models here.
class Car (models.Model):
    ttype = models.CharField(max_length=140)
    year =  models.CharField(max_length=140)
    colour  =  models.CharField(max_length=140)
    price = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
    created = models.DateTimeField(auto_now_add = True)


    def __str__(self):
		return str(self.ttype)
