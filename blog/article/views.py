from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from article.models import Article, ArticleType,Comments


def index(request):
    return HttpResponse('hello')


def show_html(request):
    articles = Article.objects.all().order_by('-addtime')
    types = ArticleType.objects.all()

    return render(request, 'index.html', context={'articles': articles, 'types': types})


def show_type(request):
    types = ArticleType.objects.all()
    id = request.GET.get('id')
    type_obj = ArticleType.objects.get(id=id)
    articles = type_obj.article_set.all()

    return render(request, 'type.html', context={'types': types, 'articles': articles, })


def show_detail(request):


    id = request.GET.get('id')
    article = Article.objects.get(pk=id)
    article.clicknum = article.clicknum+1
    article.save()
    types = ArticleType.objects.all()


    return render(request, 'detail.html', context={'article': article, 'types': types})

def show_about(request):
    return render(request,'about.html')

def show_login(request):
    return render(request,'demo02.html')
def show_aboutme(request):
    return render(request,'about.html')

def add_comment(request):
    nick_name=request.POST.get('uname')
    content = request.POST.get('saytext')
    id=request.POST.get('id')

    comment=Comments()
    comment.nick_name=nick_name
    comment.content = content
    comment.article_id =id
    comment.save()
    article = Article.objects.get(pk=id)
    types = ArticleType.objects.all()

    return render(request,'detail.html',context={'types':types,'article':article})

