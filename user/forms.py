from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class person_form(forms.Form):
        login = forms.CharField(max_length=100, label='Логин', widget=forms.TextInput(attrs={
                'class': 'auth-f',
                'placeholder': 'Введите логин',
            }))
        password = forms.CharField(max_length=100, label='Пароль', widget=forms.PasswordInput(attrs={
                'class': 'auth-f1',
                'placeholder': 'Введите пароль',
            }))


class register_form(UserCreationForm):
        username = forms.CharField(max_length=120, label='Логин', widget=forms.TextInput(attrs={'class': 'username', 'placeholder': 'Введите логин'}))
        password1 = forms.CharField(max_length=120, label='Пароль', widget=forms.PasswordInput(attrs={'class': 'password1', 'placeholder': 'Придумайте пароль'}))
        password2 = forms.CharField(max_length=120, label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'password2', 'placeholder': 'Повторите пароль'}))
        # email = forms.CharField(max_length=50, label='Почта', widget=forms.EmailInput(attrs={'class': 'email_field',
        #             'placeholder': 'Введите почту'}))

        class Meta: 
            model = User
            fields = ('username', 'password1', 'password2')