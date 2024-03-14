from django.shortcuts import render
from django.http import HttpResponse


def url1(request):
    return HttpResponse("Hello, world. You're at the Earth")


def url2(request):
    return HttpResponse("Hello, world. You're at the moon")
