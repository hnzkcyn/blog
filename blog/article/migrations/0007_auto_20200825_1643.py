# Generated by Django 3.0.8 on 2020-08-25 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_article_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='desc',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='comments',
            name='nick_name',
            field=models.CharField(max_length=140),
        ),
    ]
