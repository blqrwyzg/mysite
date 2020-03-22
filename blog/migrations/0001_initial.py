# Generated by Django 2.2.8 on 2020-03-21 16:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=20, verbose_name='标签')),
                ('release', models.CharField(choices=[('n', '未发布'), ('y', '已发布')], default='未发布', max_length=2, verbose_name='是否发布')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='文章标题')),
                ('introduction', models.CharField(max_length=100, verbose_name='文章简介')),
                ('body', models.TextField(verbose_name='内容')),
                ('release', models.CharField(choices=[('n', '未发布'), ('y', '已发布')], default='未发布', max_length=2, verbose_name='是否发布')),
                ('creation_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('save_time', models.DateTimeField(auto_now=True, verbose_name='最后修改日期')),
                ('hit_count', models.BigIntegerField(default=0, verbose_name='点击次数')),
                ('label', models.ManyToManyField(max_length=30, related_name='article', to='blog.label', verbose_name='文章标签')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'ordering': ['-creation_time'],
            },
        ),
    ]
