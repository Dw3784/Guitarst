from django.shortcuts import render, redirect
from .models import *
from catalog.models import *

# Основное отображение корзины
def main_cart(request):
    if cart_Model.objects.filter(user=request.user).count() != 0:

        user_cart = cart_Model.objects.filter(user=request.user)
        user_prices = cart_Model.objects.filter(user=request.user).values('price')# цены на товары
        user_products = cart_Model.objects.filter(user=request.user).values('product')# продукты
        user_quantityes = cart_Model.objects.filter(user=request.user).values('quantity')

        prices = []
        for i in range(len(user_prices)):
            prices.append(user_prices[i]['price'])

        products = []
        for i in range(len(user_products)):
            products.append(user_products[i]['product'])

        quantityes = []
        for i in range(len(user_quantityes)):
            quantityes.append(user_quantityes[i]['quantity'])


        user_dict = {
            'prices': prices,
            'products': products,
            'quantityes': quantityes,
        }

        full_price = 0
        for i in range(len(prices)):
            full_price += user_prices[i]['price']# общая стоимость

        count = len(user_dict['prices'])
        print(user_dict)
        context = {
            'title': 'UserCart',
            'full_price': full_price,
            'user_dict': user_dict,
            'count': count,
        }

        return render(request, 'main_cart.html')
    
    elif User.is_authenticated:
        return render(request, 'empty_cart.html')
    
    else:
        return redirect('user:reg_or_auth')


# Для пустой корзины
def empty_cart(request):
    return redirect('catalog:Main') # При нажатии на кнопку


# Создание корзины
def create_cart(request, slug):
    object = pproducts.objects.filter(slug=slug)# объект модели продуктов

    price = object.values('price')
    price = int(price[0]['price'])# цена товара

    product = object.values('name')[0]['name']# товар, добавляемый в коризну

    user_cart = cart_Model.objects.filter(user=request.user, product=product)# корзина пользователя
    
    if user_cart.exists():

        try:
            quantity = user_cart.values('quantity')
            quantity = quantity[0]['quantity']# количество товара
        except:
            print('Корзина не создана')

        user_product = user_cart.values('product')# товар в корзине

        if user_product[0]['product'] == product:
            quantity += 1
            user_cart.values('quantity').update(quantity=quantity)

    else:
       cart_Model.objects.create(product = product, quantity = 1, user = request.user, price = price)# создание записи в базе данных

    context = {
        'title': 'Cart',
        'text': 'Товар добавлен в корзину',
    }

    return render(request, 'cart.html', context)


# Удаление товара из корзины
def delete_cart(request, slug):
    pass


# Обновление корзины
def update_cart(request, slug):
    pass