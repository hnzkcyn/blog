from django.contrib import admin


# Register your models here.
from article.models import Article
from article.models import ArticleType


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','content','desc']

class ArticleTypeAdmin(admin.ModelAdmin):
    list_display = ['name','addtime']




admin.site.register(Article,ArticleAdmin)
admin.site.register(ArticleType,ArticleTypeAdmin)