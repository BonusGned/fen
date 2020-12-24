from django.db import models
from django.contrib.contenttypes.models import ContentType


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(verbose_name='Image', blank=True, upload_to='product/')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stock = models.PositiveIntegerField('Percentage discount', default=0)
    available = models.BooleanField(default=True)

    def str(self):
        return self.title

    def get_sale(self):
        return int(self.price * (100 - self.stock) / 100)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'