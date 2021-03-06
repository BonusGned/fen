# Generated by Django 3.1.4 on 2020-12-25 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0007_auto_20201222_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_products', models.PositiveIntegerField(default=0)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Total price')),
                ('in_order', models.BooleanField(default=True)),
                ('for_anonymous_user', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone number')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='product/', verbose_name='Image'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone')),
                ('address', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Address')),
                ('status', models.CharField(choices=[('new', 'New order'), ('in_progress', 'Order in processing'), ('is_ready', 'Order is ready'), ('completed', 'Order in processing')], default='new', max_length=100, verbose_name='Order status')),
                ('buying_type', models.CharField(choices=[('self', 'Pickup'), ('delivery', ' Delivery')], default='self', max_length=100, verbose_name='Order type')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Comment to order')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Order creation date')),
                ('order_date', models.DateField(default=django.utils.timezone.now, verbose_name='Date of receipt of the order')),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.cart', verbose_name='Cart')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_orders', to='shop.customer', verbose_name='Customer')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='orders',
            field=models.ManyToManyField(related_name='related_order', to='shop.Order', verbose_name='Customer orders'),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Total price')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_products', to='shop.cart', verbose_name='Cart')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.customer', verbose_name='Customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='Product')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.customer', verbose_name='Owner'),
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(related_name='related_cart', to='shop.CartProduct', verbose_name='Cart'),
        ),
    ]
