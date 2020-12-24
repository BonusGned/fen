from django.shortcuts import render
from django.views.generic import ListView

from .models import Product, Category


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.filter(available=True)
    template_name = 'base.html'


class CategoryListView(ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = 'base.html'


# class LoginView()
