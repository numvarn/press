from django.shortcuts import render, HttpResponse

# Create your views here.
from . import models


def home(request):
    context = {}
    context['articles'] = models.Article.objects.all().order_by('id')

    return render(request, 'home.html', context)


def author(request):
    return render(request, 'author.html')


def detail(request, id):
    context = {}
    articles = models.Article.objects.filter(id=id)
    for article in articles:
        context['article'] = article
    return render(request, 'article_detail.html', context)
