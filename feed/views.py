from django.shortcuts import render
from .models import Article,Comment,HashTag

def index(request):
    article_list=Article.objects.all()

    ctx={
        "article_list":article_list,
    }
    return render(request,"index.html",ctx)

def detail(request,article_id):
    article=Article.objects.get(id=article_id)
    ctx={
        "article":article
    }
    return render(request,"detail.html",ctx)
