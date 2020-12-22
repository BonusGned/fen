from django.shortcuts import render
from django.views.generic import ListView

from .models import Product


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.filter(available=True)
    template_name = 'shop/base.html'

