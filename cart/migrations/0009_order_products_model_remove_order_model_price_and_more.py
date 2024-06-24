# Generated by Django 5.0.2 on 2024-06-20 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_alter_order_model_delivery_choice_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_products_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50, null=True, verbose_name='Пользователь')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, null=True, verbose_name='Цена товара')),
                ('product', models.CharField(max_length=120, null=True, verbose_name='Товар')),
                ('quantity', models.PositiveIntegerField(null=True, verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'Продукты заказа',
                'verbose_name_plural': 'Продукты заказов',
            },
        ),
        migrations.RemoveField(
            model_name='order_model',
            name='price',
        ),
        migrations.RemoveField(
            model_name='order_model',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order_model',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='order_model',
            name='user',
        ),
    ]