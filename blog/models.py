from django.db import models
from django.utils import timezone
# Create your models here.

class article(models.Model):


    Article_publishing_options = {
        ('y','yes'),
        ('n','no')

    }
    title = models.CharField(max_length=30,verbose_name='文章标题')

    label = models.CharField(max_length=30,verbose_name='文章标签')

    body = models.CharField(max_length=2000)

    release = models.CharField(max_length=2,choices=Article_publishing_options,verbose_name='是否发布')

    creation_time = models.DateTimeField(auto_now_add=timezone.now(),verbose_name='创建时间')

    save_time = models.DateTimeField(auto_now=timezone.now(),verbose_name='保存日期')

    hit_count = models.BigIntegerField(default=0,verbose_name='点击次数')