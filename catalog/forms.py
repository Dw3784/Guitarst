from .models import person
from django .forms import ModelForm, TextInput, NumberInput

class person_form(ModelForm):
    class Meta:
        model = person
        fields = ['name', 'age']

        widgets = {
            "name": TextInput(attrs={
                'class': 'auth-f',
                'placeholder': 'Введите своё имя',
            }),

            "age": NumberInput(attrs={
                'class': 'auth-f',
                'placeholder': 'Введите свой возраст'
            }),
        }
