from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class person_form(forms.Form):
        login = forms.CharField(max_length=100, label='Логин')
        password = forms.CharField(max_length=100, label='Пароль')

        widgets = {
            "login": forms.TextInput(attrs={
                'class': 'auth-f',
                'placeholder': 'Введите логин',
            }),

            "password": forms.PasswordInput(attrs={
                'class': 'auth-f',
                'placeholder': 'Введите пароль'
            }),
        }


class register_form(UserCreationForm):
        username = forms.CharField(max_length=120, label='Логин')
        password1 = forms.CharField(max_length=120, label='Пароль')
        password2 = forms.CharField(max_length=120, label='Повтор пароля')

        class Meta: 
            model = User
            fields = ('username', 'password1', 'password2')
            widgets = {
                   'username': forms.TextInput(attrs={'class': 'username'}),
                   'password1': forms.PasswordInput(attrs={'class': 'password1'}),
                   'password2': forms.PasswordInput(attrs={'class': 'password2'}),
            }