from django.shortcuts import render
from .models import Article

def index(request):
    search_query = request.GET.get('search', '')

    if search_query:
        articles = Article.objects.filter(article_title__icontains=search_query)
    else:
        articles = Article.objects.all()
    return render(request, 'articles/articles.html', context={'articles': articles})

def detail(request, article_id):
    a = Article.objects.get(id = article_id)
    return render(request,'articles/detail.html', context={'article': a})