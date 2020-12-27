from django.shortcuts import render
from django.views.generic import ListView, View, DetailView

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
        return render(request, 'base.html', context)


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


class ProductDetailView(CartMixin, DetailView):
    context_object_name = 'product'
    template_name = 'product_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = self.cart
        return context


class CategoryDetailView(CartMixin, DetailView):
    model = Category
    queryset = Category.objects.all()
    context_object_name = 'category'
    template_name = 'category_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = self.cart
        return context
