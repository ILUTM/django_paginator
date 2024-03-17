from django import forms
from .models import *


class UpdateItemForm(forms.Form):
    description = forms.CharField(max_length=1024*8, label='Description')
    price = forms.DecimalField(
        decimal_places=2,
        max_digits=10,
        label='Price'
    )

