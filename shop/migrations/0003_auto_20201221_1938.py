# Generated by Django 3.1.4 on 2020-12-21 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_delete_specification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(),
        ),
    ]
