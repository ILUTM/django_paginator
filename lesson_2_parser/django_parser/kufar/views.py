from django.shortcuts import render
from django.http import HttpResponse


def url1(request):
    return HttpResponse("You are here and not there")


def url2(request):
    return HttpResponse("You are there and not here")


def home(request):
    return HttpResponse("Welcome to the homepage!")
