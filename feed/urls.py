from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns=[
        url(r'^$',views.index,name='index'),
        url(r'^(?P<article_id>[0-9]+)/$',views.detail,name='index'),
        url(r'^DeleteComment/$',views.del_comment,name='index'),
        url(r'^lotto/$',views.lotto,name='index'),
        url(r'^dellotto/$',views.delete_Lotto,name='index'),
        url(r'^blog/$',views.newblog,name='index'),
        ]
