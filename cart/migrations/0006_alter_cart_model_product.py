# Generated by Django 5.0.2 on 2024-06-09 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_cart_model_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_model',
            name='product',
            field=models.CharField(max_length=120, verbose_name='Товар'),
        ),
    ]
