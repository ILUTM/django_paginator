from django import forms
from .models import *


class UpdateItemForm(forms.Form):
    description = forms.CharField(max_length=1024*8)
    price = forms.IntegerField(max_digits=100)

