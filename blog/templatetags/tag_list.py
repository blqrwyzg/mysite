from django import template
from blog.models import label
from django.db.models import Count
register = template.Library()


@register.inclusion_tag('blog/html/tag/tags.html')
def Lable_Tag_Name():
    tag_name_list =  label.label_release.annotate(Count('article')).order_by('article__count')
    return {'tag_name_list':tag_name_list}