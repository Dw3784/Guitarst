from django.contrib import admin
from .models import pproducts, categories

#admin.site.register(person)
#admin.site.register(pproducts)

@admin.register(pproducts)
class pproductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(categories)
class categoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}