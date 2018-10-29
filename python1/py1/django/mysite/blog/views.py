from django.shortcuts import render
from .models import BlogArticles
# Create your views here.
def blog_title(request):
    blogs=BlogArticles.objects.all()
    return render(request,'blog/titles.html',{'blogs':blogs}) #创建视图跳转连接，并把blogs绑定到request,key为“blogs”
