from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Furniture
from forms import UpdateItemForm


def show_all(request):
    furniture_list = Furniture.objects.order_by('-parse_datetime')
    return render(
        request,
        'kufar/show_all.html',
        {'furniture_list': furniture_list}
    )


def show_all_admin(request):
    furniture_list = Furniture.objects.order_by('id')
    form = UpdateItemForm()
    return render(
        request,
        'kufar/show_all_admin.html',
        {'furniture_list': furniture_list}
    )


def show_item(request, item_id):
    item = Furniture.objects.get(id=item_id)
    return render(
        request,
        'kufar/show_item.html',
        {'item': item}
    )


def main(request):
    return redirect('main')


def page_not_found(request, exception):
    return redirect('main')


