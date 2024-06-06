from django.shortcuts import render, redirect
from .models import *
from catalog.models import *

# Create your views here.
#Основное отображение корзины
def main_cart(request):
    if cart_Model.objects.count() != 0:
        return render(request, 'cart.html')
    
    elif cart_Model.objects.values('user').count() != 0:
        return render(request, 'empty_cart.html')
    
    else:
        return redirect('user:reg_or_auth')
    

# Для пустой корзины
def empty_cart(request):
    return redirect('catalog:Main') #При нажатии на кнопку


def create_cart(request, slug):
    object = pproducts.objects.filter(slug=slug)
    price = object.values('price')
    price = int(price[0]['price'])#цена товара

    product = object.values('name')
    product = product[0]['name']#название товара

    #пользователь
    #количество
    
    #cart_Model(user = user, product = pruduct, quantity = quantity)

    return render(request, 'cart.html')

def delete_cart(request, slug):
    pass


def update_cart(request, slug):
    pass