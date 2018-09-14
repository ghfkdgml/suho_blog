from django.shortcuts import render
from .models import Article,Comment,HashTag

def index(request):

    category=request.GET.get("category")

    if category:
        article_list=Article.objects.filter(category=category)
    else:
        article_list=Article.objects.all()
    hashtag_list=HashTag.objects.all()
    article_ext=Article.objects.all()
    category_list=set([
        (article.category,article.get_category_display()) for article in article_ext
        ])


    ctx={
        "article_list":article_list,
        "hashtag_list":hashtag_list,
        "category_list":category_list,
    }
    return render(request,"index.html",ctx)

def detail(request,article_id):
    article=Article.objects.get(id=article_id)
    ctx={
        "article":article
    }
    return render(request,"detail.html",ctx)
