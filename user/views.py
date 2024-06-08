from typing import Any
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import *

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
            # cd = form.cleaned_data
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