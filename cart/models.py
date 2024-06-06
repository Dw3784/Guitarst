from django.db import models
from user.models import *
from catalog.models import *

# Create your models here.
class cart_Model(models.Model):
    user = models.ForeignKey(person, on_delete=models.CASCADE, verbose_name = 'Пользователь')
    product = models.ForeignKey(pproducts, on_delete=models.CASCADE, verbose_name = 'Товар')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name = 'Количество')
    add_date = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата добавления')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'Корзина пользователя: {self.user}| Товар: {self.quantity} в количестве: {self.count}'