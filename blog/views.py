from django.shortcuts import render
from blog.models import article,label
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger,InvalidPage
from django.views.generic import ListView,DetailView
import markdown
# Create your views here.



#首页
# def index(request):
#     article_list = blog.article_release.all()
#     paginator = Paginator(article_list,5)
#
#     page = request.GET.get('page')
#
#     try:
#         contacts = paginator.page(page)
#
#     except PageNotAnInteger:
#         contacts = paginator.page(1)
#
#     except EmptyPage:
#         contacts = paginator.page(paginator.num_pages)
#
#
#     return render(request, 'blog/html/index.html',locals())


# 类 - 首页
class IndexView(ListView):
    # 展示的列表
    queryset = article.article_release.all()
    template_name = 'blog/html/index.html'
    context_object_name = 'contacts'
    paginate_by = 10






# 具体内容页面
def specific_article(request,id):
    page = get_object_or_404(article,id=id)
    return render(request,'blog/html/article_page.html',{'page':page})

#具体页面
# class Specific_article(DetailView):
#     template_name = 'blog/html/article_page.html'
#     queryset = blog.article_release.all()
#     context_object_name = 'page'




        

#纪录
def page_label(request):
    time_page = article.article_release.all()
    return render(request,'blog/html/label.html',{'time_page':time_page})


#关于我
def about_me(request):
    me_page = get_object_or_404(article,title='About_me')
    return render(request,'blog/html/article_page.html',{'page':me_page})


#标签页
# def tag_list(request,id):
#     #获取标签
#     tag = label.objects.get(id = id)
#     #查找标签下的文章
#     tag_articles = tag.blog.all()
#     return render(request,'blog/html/tag_list.html',{'tag_lists':tag_articles,'tage_name':tag.tag_name})

#标签页 - 类视图

class Tag_list(ListView):

    template_name = 'blog/html/tag_list.html'
    context_object_name = 'tag_lists'

    def get_queryset(self):
        self.tag = get_object_or_404(label,id = self.kwargs['id'])
        return self.tag.article.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Tag_list, self).get_context_data()
        self.tag = get_object_or_404(label,id=self.kwargs['id'])
        context['tage_name'] = self.tag.tag_name
        return context



