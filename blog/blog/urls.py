"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.views.static import serve

from article.views import index,show_html,show_type,show_detail,show_login,add_comment,show_aboutme
from blog import settings

urlpatterns = [
    path('admin/', admin.site.urls),



    #path('', index),
    path('', show_html,name='index'),
    path('type/',show_type,name='types'),
    path('detail/',show_detail,name='detail'),
    path('login/',show_login,name='login'),
    path('addcomment/',add_comment,name='addcomment'),
    path('aboutme',show_aboutme,name='aboutme'),

re_path(r'media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),


]
