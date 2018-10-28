from django.shortcuts import render
from .models import Article,Comment,HashTag,Lotto
from django.http import HttpResponseRedirect
from django.contrib import messages
from random import *
import time

article_ext=Article.objects.all()
hashtag_list=HashTag.objects.all()
hash_num=len(hashtag_list)
category_list=set([
    (article.category,article.get_category_display()) for article in article_ext
    ])
category_num={"dv":0,"ps":0,"etc":0}
for article in article_ext:
    if article.category=="dv":
        category_num["dv"]+=1
    elif article.category=="ps":
        category_num["ps"]+=1
    elif article.category=="etc":
            category_num["etc"]+=1

print(category_list)

def index(request):

    category=request.GET.get("category")

    if category:
        article_list=Article.objects.filter(category=category)
    else:
        article_list=Article.objects.all()


    ctx={
        "article_list":article_list,
        "hashtag_list":hashtag_list,
        "category_list":category_list,
        "hash_num":hash_num,
        "category_num":category_num,
    }
    return render(request,"index.html",ctx)

def detail(request,article_id):
    # if request.method=="GET":
    article=Article.objects.get(id=article_id)
    comment_list=article.article_comments.all()
    article_ext=Article.objects.all()
    hashtag_list=HashTag.objects.all()
    category_list=set([
        (article.category,article.get_category_display()) for article in article_ext
        ])
    ctx={
        "article":article,
        "category_list":category_list,
        "hashtag_list":hashtag_list,
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
        print(request.POST)
        messages.info(request,'댓글 추가 완료!')
        return HttpResponseRedirect("/{}/".format(article_id))
    # print (request)        # print (username,content)
    return render(request,"detail.html",ctx)

def del_comment(request):
    id=request.GET['id']
    article_id=request.GET['article_id']
    print(request.GET)
    p=Comment.objects.filter(id=id)
    p.delete()
    # return HttpResponseRedirect("/{}/".format(request.GET.get['article_id']))
    # messages.info(request,'댓글이 삭제되었습니다!')
    messages.info(request,'댓글 삭제 완료!')
    return HttpResponseRedirect("/{}/".format(article_id))

def lotto(request):
    #lotto_list
    if request.POST:
        lotto_day=time.strftime('%Y-%m-%d')
        lotto_num=choiceNum()
        Lotto.objects.create(day=lotto_day,lotto=lotto_num)
    # elif request.GET:
    #     id=request.GET['id']
    #     Lotto.objects.filter(id=id).delete()
    #     messages.info(request,'로또번호 삭제 완료!')
    #     return HttpResponseRedirect("/lotto/")

    lotto_list=Lotto.objects.all()
    ctx={
        "category_list":category_list,
        "hashtag_list":hashtag_list,
        "lotto_list":lotto_list,
    }
    return render(request,"lotto.html",ctx)

def delete_Lotto(request):
    id=request.GET['id']
    print(id)
    p=Lotto.objects.filter(id=id)
    p.delete()
    messages.info(request,'로또번호 삭제 완료!')
    return HttpResponseRedirect("/lotto/")

def newblog(request):
    if request.POST:
        title=request.POST.get("title")
        content=request.POST.get("content")
        Article.objects.create(
            title=title,
            content=content,
        )
        messages.info(request,'블로그 추가 완료!')
        ctx={
            "category_list":category_list,
            "hashtag_list":hashtag_list,
        }
        return HttpResponseRedirect("/blog/")
    else:
        ctx={
            "category_list":category_list,
            "hashtag_list":hashtag_list,
        }
        return render(request,"blog.html",ctx)


def choiceNum():
    totalNum=[]
    TOTAL={1:[1]*145,2:[2]*132,3:[3]*128,4:[4]*136,5:[5]*127,6:[6]*128,7:[7]*131,8:[8]*131,9:[9]*101,10:[10]*137,11:[11]*133,12:[12]*137,13:[13]*138,14:[14]*131,15:[15]*128,16:[16]*126,17:[17]*139,18:[18]*128,19:[19]*127,20:[20]*140,21:[21]*130,22:[22]*101,23:[23]*111,24:[24]*131,25:[25]*125,26:[26]*129,27:[27]*148,28:[28]*111,29:[29]*109,30:[30]*120,31:[31]*131,32:[32]*112,33:[33]*136,34:[34]*144,35:[35]*122,36:[36]*126,37:[37]*133,38:[38]*123,39:[39]*128,40:[40]*137,41:[41]*114,42:[42]*120,43:[43]*147,44:[44]*125,45:[45]*128}
    for i in range(len(TOTAL)):
        totalNum=totalNum+TOTAL[i+1]
    ret=[]
    for i in range(6):
        num=choice(totalNum)
        ret.append(num)
        for j in range(totalNum.count(num)):
            totalNum.remove(num)
    return sorted(ret)


# def lotto_page(request):
#     day=request.POST.get("day")
#
#     messages.info(request,'번호 생성 완료')
