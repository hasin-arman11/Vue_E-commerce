# Generated by Django 4.2.3 on 2024-01-04 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordereditems',
            name='price',
        ),
        migrations.RemoveField(
            model_name='ordereditems',
            name='quantity',
        ),
    ]
