from django.db import models
from user.models import *
from catalog.models import *
from django.contrib.auth.models import User

# Create your models here.
class cart_Model(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Пользователь', db_constraint = False)
    user = models.CharField(max_length=120, null=True, verbose_name='Пользователь')
    product = models.CharField(max_length=120, verbose_name = 'Товар')
    price = models.IntegerField(null=True)
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name = 'Количество')
    add_date = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата добавления', null = True)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'Корзина пользователя: {self.user} | Товар: {self.product} в количестве: {self.quantity}'
    
    def product_price(self):
        return round(self.price * self.quantity, 2)