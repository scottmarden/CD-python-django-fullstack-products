# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import Product

# Create your views here.
def index(request):
	#Commenting out adding of products, so that it doesn't reload on every page refresh. Can also do this in the python shell
		# Product.objects.create(name="Campbells Tomato Soup", description="A delicious can of the tomato soup you know and love!", weight="8oz", price=2.00, cost=.50, category="Canned Foods")

		# Product.objects.create(name="Pirate's Booty", description="A fun twist on cheese puffs!", weight="16oz", price=4.99, cost=1.25, category="Snacks")

		# Product.objects.create(name="Macbook Pro", description="A reliable, powerful, overpriced status symbol that you can use to check your facebook", weight="3.02lbs", price=2000.00, cost=14.50, category="Luxury Items")
		
	#print info about products
	products = Product.objects.all()
	print products
	for product in products:
		print product.name, product.description, product.weight, product.price, product.cost, product.category
	return render(request, 'products_app/index.html')
