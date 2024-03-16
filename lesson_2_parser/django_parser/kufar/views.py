from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Furniture


def show_all(request):
    furniture_list = Furniture.objects.order_by('price')
    return render(
        request,
        'kufar/show_all.html',
        {'furniture_list': furniture_list}
    )

def main(request):
    return redirect('main')


def page_not_found(request, exception):
    return redirect('main')


