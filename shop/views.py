from django.shortcuts import render
from django.views.generic import ListView, View

from .mixins import CartMixin
from .models import Product, Category


class BaseView(CartMixin, View):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        products = Product.objects.filter(available=True)
        context = {
            'categories': categories,
            'products': products,
            'cart': self.cart
        }
        return render(request, 'base.html', context=context)


# class ProductListView(ListView):
#     model = Product
#     queryset = Product.objects.filter(available=True)
#     template_name = 'base.html'
#
#
# class CategoryListView(ListView):
#     model = Category
#     queryset = Category.objects.all()
#     template_name = 'base.html'


# class LoginView()
