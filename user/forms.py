from django import forms
from django.contrib.auth.forms import UserCreationForm
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
        class Meta(UserCreationForm.Meta): 
            model = person