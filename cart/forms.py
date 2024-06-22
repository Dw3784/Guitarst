from django import forms
from django.core.exceptions import ValidationError

class order_form(forms.Form):
    Paid_choice = (
        ('При получении', 'При получении'),
        ('Онлайн', 'Онлайн'),
    )

    Delivery_choice = (
        ('Самовывоз', 'Самовывоз'),
        ('Курьером', 'Курьером'),
    )

    phone_number = forms.CharField(max_length='60', label='Номер телефона', widget=forms.TextInput(attrs={'class': 'number_input', 'placeholder': 'Введите номер телефона'}))
    first_name = forms.CharField(max_length='120', label='Имя', widget=forms.TextInput(attrs={'class': 'first_input', 'placeholder': 'Введите ваше имя'}))
    last_name = forms.CharField(max_length='120', label='Фамилия', widget=forms.TextInput(attrs={'class': 'second_input', 'placeholder': 'Введите вашу фамилию'}))
    address = forms.CharField(max_length='120', label='Адрес доставки', widget=forms.TextInput(attrs={'class': 'addres_input', 'placeholder': 'Введите адрес доставки'}))
    paid_choice = forms.ChoiceField(label='Способ оплаты', choices=Paid_choice)
    delivery_choice = forms.ChoiceField(label='Способ доставки', choices=Delivery_choice)

    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']

        if not data.isdigit():
            raise forms.ValidationError("Номер телефона должен содержать только цифры")
            
        if len(data) != 10 and data[0] != '+' or data[0] == '+' and len(data) != 11:
            
            self.add_error('phone_number', "Номер телефона должен содержать 10 цифр")
        return data