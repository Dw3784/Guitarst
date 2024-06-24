from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.core.validators import *
from django.core.exceptions import *

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
    username = forms.CharField(max_length=120, label='Логин', widget=forms.TextInput(attrs={
        'class': 'username', 'placeholder': 'Введите логин'}))
    
    password1 = forms.CharField(max_length=120, label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'password1', 'placeholder': 'Придумайте пароль'}))
    
    password2 = forms.CharField(max_length=120, label='Повтор пароля', widget=forms.PasswordInput(
        attrs={'class': 'password2', 'placeholder': 'Повторите пароль'}))

    class Meta: 
        model = User
        fields = ('username', 'password1', 'password2')

class add_email_form(forms.Form):
    email = forms.EmailField(max_length=120, label='Почта', widget=forms.EmailInput(attrs={'placeholder': 'Введите почту'}))