from django.forms import ModelForm
from .models import Items
from django import forms

class ItemForm(ModelForm):
    class Meta:
        model = Items
        fields = ('name', 'quantity','image',)
        labels = {
            'name': 'Name of Item',
            'quantity': 'Number of Items',
        }