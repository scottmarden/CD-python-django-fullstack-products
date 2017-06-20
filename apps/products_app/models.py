# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length = 255)
	description = models.TextField()
	weight = models.CharField(max_length = 45)
	price = models.FloatField()
	cost = models.FloatField()
	category = models.CharField(max_length = 100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
