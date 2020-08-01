from datetime import datetime

from django.db import models


# Create your models here.
class Article(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80, null=False)
    desc = models.CharField(max_length=255, null=False)
    content = models.TextField()
    likes = models.IntegerField(default=0)
    clicknum = models.IntegerField(default=0)
    addtime = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return self.title


class ArticleType(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    addtime = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return self.name





    


