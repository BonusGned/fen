from django.contrib import admin
from .models import Category, Product, Cart, CartProduct, Order, Customer


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('title', 'id')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'slug', 'image', 'category', 'price',
        'description', 'created_at', 'updated_at', 'stock',
        'available',
    )
    list_display_links = ('title', 'id')
    prepopulated_fields = {'slug': ('title',)}


admin.register(Cart)(admin.ModelAdmin)
admin.register(CartProduct)(admin.ModelAdmin)
admin.register(Order)(admin.ModelAdmin)
admin.register(Customer)(admin.ModelAdmin)
