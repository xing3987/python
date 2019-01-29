from django.shortcuts import render
from .models import BlogArticles
from django.shortcuts import render,get_object_or_404  #导入错误界面的函数
# Create your views here.
def blog_title(request):
    blogs=BlogArticles.objects.all()
    return render(request,'blog/titles.html',{'blogs':blogs}) #创建视图跳转连接，并把blogs绑定到request,key为“blogs”

def blog_article(request,article_id):
    #article=BlogArticles.objects.get(id=article_id)
    article=get_object_or_404(BlogArticles,id=article_id)
    pub=article.publish
    return render(request,'blog/content.html',{"article":article,"publish":pub})