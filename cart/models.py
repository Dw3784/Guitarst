from django.db import models
from user.models import *
from catalog.models import *
from django.contrib.auth.models import User

# Модель корзины
class cart_Model(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Пользователь', db_constraint = False)
    user = models.CharField(max_length=120, null=True, verbose_name='Пользователь')
    product = models.CharField(max_length=120, verbose_name='Товар')
    price = models.IntegerField(null=True)
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    add_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления', null = True)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'Корзина пользователя: {self.user} | Товар: {self.product} в количестве: {self.quantity}'
    
    def product_price(self):
        return round(self.price * self.quantity, 2)
    
    def total_quantity(self):
        return sum(product.quntity for product in self)
    

# Модель заказа
class order_Model(models.Model):
    phone_number = models.CharField(max_length=60, verbose_name='Номер телефона')
    first_name = models.CharField(max_length=120, verbose_name='Имя')
    last_name = models.CharField(max_length=120, verbose_name='Фамилия')
    address = models.CharField(max_length=120, verbose_name='Адрес доставки')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата оформления')
    paid_choice = models.TextField(default=False, verbose_name='Оплата при получении')
    delivery_choice = models.TextField(default=False, verbose_name='Требуется доставка')
    status = models.CharField(max_length=30, default='В обработке')
    user = models.CharField(max_length=50, verbose_name='Пользователь', null=True)
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ №: {self.pk} | пользователя: {self.user}'
    

class order_products_Model(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена товара', null=True)
    product = models.CharField(max_length=120, verbose_name='Товар', null=True)
    quantity = models.PositiveIntegerField(verbose_name='Количество', null=True)
    order = models.ForeignKey(to=order_Model, on_delete=models.CASCADE, verbose_name='Заказ', null=True)

    class Meta:
        verbose_name = 'Продукты заказа'
        verbose_name_plural = 'Продукты заказов'