from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def login (request):
    return HttpResponse("<h1> This is sign-In page. </h1>")


def register(request):
    return HttpResponse("<h1> This is sign-up page</h1>")