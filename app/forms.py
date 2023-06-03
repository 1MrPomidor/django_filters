from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'expiring_date': forms.DateTimeInput(attrs={'type': 'Date'}),
            'title': forms.TextInput(attrs={'placeholder': 'Введите названия'})
        }
