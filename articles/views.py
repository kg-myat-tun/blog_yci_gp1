from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render

from articles.models import Article, Category
# Create your views here.


def index(request):
    articles = Article.objects.all().order_by('-id')
    categories = Category.objects.all
    return render(request,'articles/index.html',{ 'articles' : articles ,'categories':categories});

def article_detail(request,id):
    article = get_object_or_404(Article,id=id)
    categories = Category.objects.all
    return render(request, 'articles/article_detail.html' , {'article': article,'categories':categories})

def article_by_category(request,id):

    articles = Article.objects.filter( category_id = id).order_by('-id')
    categories = Category.objects.all
    return render(request, 'articles/article_by_category.html' , {'articles': articles,'categories':categories})

def contact(request):
    return render(request,'articles/contact.html')



