from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Furniture
from . forms import UpdateItemForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy


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
        {'form': form,
            'furniture_list': furniture_list}
    )


def show_item(request, item_id):
    item = Furniture.objects.get(id=item_id)
    return render(
        request,
        'kufar/show_item.html',
        {'item': item}
    )


def update_item(request, item_id):
    if request.method == 'POST':
        new_description = dict(request.POST).get('description', '')
        new_price = dict(request.POST).get('price', '')
        Furniture.objects.filter(id=item_id).update(
            description=new_description[0],
            price=new_price[0]
        )
    return redirect('items_admin')


def delete_item(request, item_id):
    Furniture.objects.filter(id=item_id).delete()
    return redirect('items_admin')


def main(request):
    return redirect('main')


def page_not_found(request, *args, **kwargs):
    return redirect('main')


def login(request):
    return render(request, 'registration/login.html')


def logout(request):
    return render(request, 'registration/logout.html')


class SignUp(CreateView):
    form_class = UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'