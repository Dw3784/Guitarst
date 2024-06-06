from django.db import models

#Товары
class pproducts(models.Model):
    name = models.CharField(max_length = 25, verbose_name = 'Название')
    description = models.TextField(blank = True, null =  True, verbose_name = 'Описание')
    price = models.DecimalField(max_digits = 8, decimal_places = 2, verbose_name = 'Цена')
    quantity = models.PositiveIntegerField(default = 0, verbose_name = 'Количество')
    image = models.ImageField(upload_to = 'images', blank = True, null =  True, verbose_name = 'Изображение')
    slug = models.SlugField(max_length = 200, unique = True, blank = True, null = True, verbose_name = 'URL')
    category = models.TextField(max_length = 50, blank = True, null = True, verbose_name = 'Категория')

    class Meta():
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


#Категории товаров
class categories(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'images', blank = True, null = True)
    slug = models.SlugField(max_length = 200, unique = True, blank = True, null = True, verbose_name = 'URL')
    category = models.TextField(max_length = 50, blank = True, null = True)
    url_name = models.TextField(max_length = 25, blank = True, null = True)

    class Meta():
        db_table = 'categories'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


    def __str__(self):
        return self.name