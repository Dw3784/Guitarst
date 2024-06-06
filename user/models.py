from django.db import models

#Модель пользователя
class person(models.Model):
    username = models.CharField(max_length=45, null=True)
    slug = models.SlugField(max_length = 200, unique = True, blank = True, null = True, verbose_name = 'URL')

    class Meta():
        db_table = 'person'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username