from django.db import models

#Модель пользователя
class person(models.Model):
    name = models.CharField(max_length = 25)
    age = models.IntegerField()
    slug = models.SlugField(max_length = 200, unique = True, blank = True, null = True, verbose_name = 'URL')
    
    class Meta():
        db_table = 'person'
        verbose_name = 'user'
        verbose_name_plural = 'users'





#Товары
class pproducts(models.Model):
    name = models.CharField(max_length = 25)
    description = models.TextField(blank = True, null =  True)
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    quantity = models.PositiveIntegerField(default = 0)
    image = models.ImageField(upload_to = 'images', blank = True, null =  True)
    slug = models.SlugField(max_length = 200, unique = True, blank = True, null = True, verbose_name = 'URL')
    category = models.TextField(max_length = 50, blank = True, null = True)

    class Meta():
        db_table = 'product'
        verbose_name = 'product'
        verbose_name_plural = 'products'

#Категории товаров
class categories(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'images', blank = True, null = True)
    slug = models.SlugField(max_length = 200, unique = True, blank = True, null = True, verbose_name = 'URL')
    category = models.TextField(max_length = 50, blank = True, null = True)

    class Meta():
        db_table = 'categories'
        verbose_name = 'category'
        verbose_name_plural = 'categories'