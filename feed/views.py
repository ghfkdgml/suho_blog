from django.shortcuts import render
from .models import Article,Comment,HashTag
from django.http import HttpResponseRedirect
from django.contrib import messages

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
    # if request.method=="GET":
    article=Article.objects.get(id=article_id)
    comment_list=article.article_comments.all()
    ctx={
        "article":article,
        # "comment_list":comment_list,
    }
    if request.method=="GET":
        pass
    elif request.method=="POST":
        if request.POST.get("del"):
            return HttpResponseRedirect("/{}/".format(article_id))
        else:
            username=request.POST.get("username")
            content=request.POST.get("content")
            Comment.objects.create(
                article=article,
                username=username,
                content=content
            )
        messages.info(request,'댓글 추가 완료!')
        return HttpResponseRedirect("/{}/".format(article_id))
    # print (request)        # print (username,content)
    return render(request,"detail.html",ctx)

def del_comment(request):
    username=request.GET['username']
    content=request.GET['content']
    id=request.GET['id']
    article_id=request.GET['article_id']
    print(article_id)
    p=Comment.objects.filter(username=username,content=content,id=id)
    p.delete()
    # return HttpResponseRedirect("/{}/".format(request.GET.get['article_id']))
    # messages.info(request,'댓글이 삭제되었습니다!')
    messages.info(request,'댓글 삭제 완료!')
    return HttpResponseRedirect("/{}/".format(article_id))

# def lotto(request):
#     lotto_list
#     ctx={}
#     return render(request,"lotto.html",ctx)
