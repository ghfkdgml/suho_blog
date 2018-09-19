from django.contrib import admin
from .models import Article,Comment,HashTag,Lotto

@admin.register(Article,Comment,HashTag,Lotto)
class FeedAdmin(admin.ModelAdmin):
    pass
