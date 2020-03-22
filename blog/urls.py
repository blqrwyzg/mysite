from django.urls import path
from . import views
from haystack.views import SearchView
urlpatterns = [
    # path('',views.index,name = 'index'),
    path('',views.IndexView.as_view(),name = 'index'),

    path('blog/<int:id>',views.specific_article,name = 'specific_article'),

    #纪录
    path('blog/list',views.page_label,name = 'page_label'),

    path('about_me',views.about_me,name ='about_me'),

    #标签
    path('tag_list/<int:id>',views.Tag_list.as_view(),name = 'tag_list'),

    path('search/',SearchView(),name = 'haystack_search'),
]
