from typing import Any
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import *
from django.core.validators import *
from cart.models import *

# Регистрация или вход
def reg_or_auth_view(request):
    context = {
        'title': 'Reg_or_auth',
        'button1': 'Авторизация',
        'button2': 'Регистрация',
    }

    return render(request, 'reg_or_auth.html', context)


# Логин
def login_view(request):
    if request.method == 'POST':
        form = person_form(request.POST)
        if form.is_valid():
            username = request.POST['login']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('catalog:Main')

    else:
        form = person_form()
            
    context = {
        'form': form,
    }
    return render(request, 'auth.html', context)


# Выход
def logout_view(request):
    logout(request)
    return redirect('user:login')


# Регистрация
class register_view(CreateView):
    template_name = 'register.html'
    form_class = register_form
    success_url = reverse_lazy('catalog:Main')


# Профиль пользователя
def profile_view(request, pk):
    user = User.objects.filter(pk=pk)# Пользователь
    try:
        order = order_Model.objects.filter(user=request.user)# Заказ
        address = order.values('address')[0]['address']# Адрес
        first_name = order.values('first_name')[0]['first_name']# Имя
        last_name = order.values('last_name')[0]['last_name']# Фамилия
        status = order.values('status')[0]['status']# Статус

    except:
        print('Нет заказов')
        address = 'address'
        first_name = 'first_name'
        last_name = 'last_name'
        status = 'status'
        order_products = 'order_products'

    order_products = []# Заказанные товары
    for i in order_products_Model.objects.all():
        order_products.append(i.product)
    
    username = user.values('username')[0]['username']# Имя пользователя
    if user.values('email').exists():
        email = user.values('email')[0]['email']# Почта

    context = {
        'username': username,
        'email': email,
        'address': address,
        'first_name': first_name,
        'last_name': last_name,
        'status': status,
        'order_products': order_products,
    }
    
    return render(request, 'profile.html', context)


# Добавление почты
def add_email(request):
    if request.method == 'POST':
        form = add_email_form(request.POST)
        if form.is_valid():
        
            email = form.cleaned_data['email']
            user = User.objects.filter(username=request.user)
            user.update(email=email)
        
            return redirect('user:profile', user.values('id')[0]['id'])
        
    else:
        form = add_email_form()

    context = {
        'form': form,
    }

    return render(request, 'email.html', context)
    

# Удаление почты
def delete_email(request):
    user = User.objects.filter(username=request.user)
    user = user.values('email').update(email='')

    return redirect(request.META['HTTP_REFERER'])