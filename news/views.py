from django.shortcuts import render, HttpResponse

# Create your views here.
from . import models


def home(request):
    context = {}
    context['articles'] = models.Article.objects.all().order_by('id')

    return render(request, 'home.html', context)


def author(request):
    return render(request, 'author.html')
