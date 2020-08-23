from django.contrib import admin


# Register your models here.
from article.models import Article
from article.models import ArticleType
from article.models import Comments


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','content','desc']

class ArticleTypeAdmin(admin.ModelAdmin):
    list_display = ['name','addtime']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['nick_name','addtime','content']





admin.site.register(Article,ArticleAdmin)
admin.site.register(ArticleType,ArticleTypeAdmin)
admin.site.register(Comments,CommentAdmin)