from django.contrib import admin

# Register your models here.

from blog.models import article,label

@admin.register(article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','introduction','release','hit_count')
    list_filter = ('label','save_time','creation_time',)
    search_fields = ('title','body')




admin.site.register(label)
