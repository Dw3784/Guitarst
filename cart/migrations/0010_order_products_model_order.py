# Generated by Django 5.0.2 on 2024-06-20 09:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_order_products_model_remove_order_model_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_products_model',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.order_model', verbose_name='Заказ'),
        ),
    ]