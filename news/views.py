from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("Home Page")


def author(request):
    return HttpResponse("Author page")
