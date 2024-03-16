from django.shortcuts import render
from django.http import HttpResponse
from .models import Furniture


def show_all(request):
    furniture_list = Furniture.objects.all().order_by('-price')
    return render(request, 'kufar/show_all.html')




