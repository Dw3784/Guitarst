from django.shortcuts import render, redirect
from .models import *
from catalog.models import *
from .forms import *
from django.db import transaction
from django.contrib import messages
from django.core.exceptions import *

# Основное отображение корзины
def main_cart(request):
    if cart_Model.objects.filter(user=request.user).count() != 0:

        user_cart = cart_Model.objects.filter(user=request.user)# корзина
        user_prices = cart_Model.objects.filter(user=request.user).values('price')# цены на товары
    
        full_price = 0# общая стоимость товаров в корзине
        for i in range(len(user_prices)):
            full_price += user_prices[i]['price']

        context = {
            'title': 'UserCart',
            'full_price': full_price,
            'user_cart': user_cart,
        }

        return render(request, 'main_cart.html', context)
    
    elif request.user.is_authenticated:
        context = {
            'title': 'Empty Cart',
        }

        return render(request, 'empty_cart.html', context)
    
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
def delete_cart(request, product_id):
    cart_Model.objects.filter(user=request.user, id=product_id).delete()

    return redirect(request.META['HTTP_REFERER'])



# Оформление и отображение заказа
def create_order(request):
    if request.method == 'POST':
        form = order_form(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_objects = cart_Model.objects.filter(user=user)

                    order = order_Model.objects.create(
                        phone_number = form.cleaned_data['phone_number'],
                        first_name = form.cleaned_data['first_name'],
                        last_name = form.cleaned_data['last_name'],
                        address = form.cleaned_data['address'],
                        paid_choice = form.cleaned_data['paid_choice'],
                        delivery_choice = form.cleaned_data['delivery_choice'],
                        user = user,
                    )

                    for cart_object in cart_objects:
                        product = cart_object.product
                        price = cart_object.price
                        quantity = cart_object.quantity
                        product_quantity = pproducts.objects.filter(name=product).values('quantity')[0]['quantity']

                        if quantity > product_quantity:
                            raise ValidationError(f'Недостаточное количество товара {product} на складе\
                                                   В наличии - {quantity}')

                        else:

                            order_products_Model.objects.create(
                                product = product,
                                price = price,
                                quantity = quantity,
                                order = order,
                            )

                            new_product_quantity = product_quantity - quantity# Обновление количества товаров
                            pproducts.objects.filter(name=product).values('quantity').update(quantity=new_product_quantity)
                            cart_objects.delete()

                    messages.success(request, 'Заказ оформлен!')
                    return redirect('user:profile', user.pk)

            except ValidationError as e:
                messages.success(request, list(e)[0])
                return redirect('cart:create_order')
                
    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }

        form = order_form(initial=initial)

    context = {
        'form': form
    }

    return render(request, 'order.html', context)