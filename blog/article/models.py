from datetime import datetime

from django.db import models

class ArticleType(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    addtime = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return self.name


# Create your models here.
class Article(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80, null=False)
    desc = models.CharField(max_length=255, null=False)
    content = models.TextField()
    likes = models.IntegerField(default=0)
    clicknum = models.IntegerField(default=0)
    addtime = models.DateTimeField(default=datetime.now)
    tid = models.ForeignKey(to=ArticleType,on_delete=models.CASCADE,default=1)
    cover = models.ImageField(upload_to='cover/',default='cover/t01.jpg')


    def __str__(self):
        return self.title



class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    nick_name = models.CharField(max_length=50)
    content = models.TextField()
    article = models.ForeignKey(to=Article,on_delete=models.CASCADE)
    addtime = models.DateTimeField(default=datetime.now)











    


