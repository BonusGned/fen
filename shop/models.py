from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.utils import timezone

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('category_detail', kwargs={'slug': self.slug})

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

    def get_absolute_url(self):
        return reverse_lazy('product_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Phone number')
    address = models.CharField(max_length=255, verbose_name='Address')
    orders = models.ManyToManyField('Order', verbose_name='Customer orders', related_name='related_order')

    def __str__(self):
        return f'Customer: {self.user.first_name} {self.user.last_name}'


class CartProduct(models.Model):
    owner = models.ForeignKey(Customer, verbose_name='Customer', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Cart', on_delete=models.CASCADE, related_name='related_products')
    product = models.ForeignKey(Product, verbose_name='Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Total price')

    def __str__(self):
        return f'Product: {self.product.title} (for cart)'


class Cart(models.Model):
    owner = models.ForeignKey(Customer, null=True, verbose_name='Owner', on_delete=models.CASCADE)
    products = models.ManyToManyField('CartProduct', verbose_name='Cart', related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=9, default=0, decimal_places=2, verbose_name='Total price')
    in_order = models.BooleanField(default=True)
    for_anonymous_user = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class Order(models.Model):
    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_READY = 'is_ready'
    STATUS_COMPLETED = 'completed'

    BUYING_TYPE_SELF = 'self'
    BUYING_TYPE_DELIVERY = 'delivery'

    STATUS_CHOICES = (
        (STATUS_NEW, 'New order'),
        (STATUS_IN_PROGRESS, 'Order in processing'),
        (STATUS_READY, 'Order is ready'),
        (STATUS_COMPLETED, 'Order in processing'),
    )

    BUYING_TYPE_CHOICES = (
        (BUYING_TYPE_SELF, 'Pickup'),
        (BUYING_TYPE_DELIVERY, ' Delivery')
    )

    customer = models.ForeignKey(Customer, verbose_name='Customer', related_name='related_orders',
                                 on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, verbose_name='First Name')
    last_name = models.CharField(max_length=100, verbose_name='Last Name')
    phone = models.CharField(max_length=20, verbose_name='Phone')
    cart = models.ForeignKey(Cart, verbose_name='Cart', on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=1024, verbose_name='Address', null=True, blank=True)
    status = models.CharField(
        max_length=100,
        verbose_name='Order status',
        choices=STATUS_CHOICES,
        default=STATUS_NEW
    )
    buying_type = models.CharField(
        max_length=100,
        verbose_name='Order type',
        choices=BUYING_TYPE_CHOICES,
        default=BUYING_TYPE_SELF
    )
    comment = models.TextField(verbose_name='Comment to order', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Order creation date')
    order_date = models.DateField(verbose_name='Date of receipt of the order', default=timezone.now)

    def __str__(self):
        return str(self.id)
