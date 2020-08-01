from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from article.models import Article


def index(request):
    return HttpResponse('hello')


def show_html(request):
    articles = Article.objects.all().order_by('-addtime')



    return render(request, 'index.html', context={'articles': articles})
