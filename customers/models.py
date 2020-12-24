from django.db import models
from django.contrib.auth import get_user_model
from orders.models import Order

User = get_user_model()


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Phone number')
    address = models.CharField(max_length=255, verbose_name='Address')
    orders = models.ManyToManyField('Order', verbose_name='Customer orders', related_name='related_order')

    def __str__(self):
        return f'Customer: {self.user.first_name} {self.user.last_name}'
