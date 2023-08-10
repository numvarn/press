from django.shortcuts import render, HttpResponse

# Create your views here.
from . import models


def home(request):
    context = {}
    context['articles'] = models.Article.objects.all().order_by('id')

    return render(request, 'home.html', context)


def author(request):
    context = {}
    authors = models.Author.objects.all().order_by('id')
    for author in authors:
        author.prefix_str = getModelChoices(
            author.prefix, models.name_prefix_choice)

    context['authors'] = authors
    return render(request, 'author.html', context)


def detail(request, id):
    context = {}
    articles = models.Article.objects.filter(id=id)
    for article in articles:
        context['article'] = article
    return render(request, 'article_detail.html', context)


def author_detail(request, id):
    context = {}
    authors = models.Author.objects.filter(id=id)
    for author in authors:
        context['author'] = author
        context['articles'] = models.Article.objects.filter(author=author)

    return render(request, 'author_detail.html', context)


def getModelChoices(number, choices):
    for items in choices:
        if items[0] == number:
            return items[1]
