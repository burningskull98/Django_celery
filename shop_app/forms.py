from django import forms
from django.core.exceptions import ValidationError
from .models import Product


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'category']
        labels = {
            'name': 'Название',
            'description': 'Описание',
            'price': 'Цена',
            'quantity': 'Количество',
            'category': 'Категория',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Введите состав'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
        }


def clean_name(self):
    name = self.cleaned_data.get('name')
    if not name:
        raise ValidationError('Это поле обязательно для заполнения.')
    if len(name) < 4:
        raise ValidationError('Название должно содержать не менее 4 символов.')
    return name


def clean_price(self):
    price = self.cleaned_data.get('price')
    if price is None:
        raise ValidationError('Это поле обязательно для заполнения.')
    if price <= 0:
        raise ValidationError('Цена должна быть положительным числом.')
    return price


def clean_description(self):
    description = self.cleaned_data.get('description')
    if description is None:
        raise ValidationError('Это поле обязательно для заполнения.')
    if len (description) < 100:
        raise ValidationError('Состав должен содержать не менее 100 символов.')
    return description


def clean_category(self):
    category = self.cleaned_data.get('category')
    if not category:
        raise ValidationError('Это поле обязательно для заполнения.')
    return category





