from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(cart_Model)

admin.site.register(order_Model)

admin.site.register(order_products_Model)