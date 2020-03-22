from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
# Create your models here.

class Article_release(models.Manager):
    '''
    article默认管理器， 查找已发布的内容
    '''
    def get_queryset(self):
        return super(Article_release, self).get_queryset().filter(release ='y')

class article(models.Model):


    Article_publishing_options = {
        ('y','已发布'),
        ('n','未发布')

    }
    title = models.CharField(max_length=50,verbose_name='文章标题')

    label = models.ManyToManyField('label',max_length=30,verbose_name='文章标签',related_name='article')

    introduction = models.CharField(max_length=100,verbose_name='文章简介')

    body = models.TextField(verbose_name='内容')

    release = models.CharField(max_length=2,choices=Article_publishing_options,verbose_name='是否发布',default='未发布')

    creation_time = models.DateTimeField(default=timezone.now,verbose_name='创建时间')

    save_time = models.DateTimeField(auto_now=True,verbose_name='最后修改日期')

    hit_count = models.BigIntegerField(default=0,verbose_name='点击次数')

    objects = models.Manager() #默认管理器

    article_release = Article_release() #自定义管理器



    def __str__(self):
        return self.title

    class Meta:
        ordering =['-creation_time']
        verbose_name = '文章'
        verbose_name_plural = verbose_name


class label_release (models.Manager):
    def get_queryset(self):
        return super(label_release, self).get_queryset().filter(release = 'y')

class label(models.Model):

    Article_publishing_options = {
        ('y','已发布'),
        ('n','未发布')

    }
    tag_name = models.CharField(max_length=20,verbose_name='标签')

    release = models.CharField(max_length=2,choices=Article_publishing_options,verbose_name='是否发布',default='未发布')

    def __str__(self):
        return self.tag_name

    objects = models.Manager()

    label_release = label_release()

    class Meta:
        verbose_name='标签'
        verbose_name_plural = verbose_name




