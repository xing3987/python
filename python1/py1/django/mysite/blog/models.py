from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class BlogArticles(models.Model):
    title=models.CharField(max_length=300) #Char字段
    author=models.ForeignKey(User,related_name="blog_posts",on_delete=models.CASCADE)  #字段外键关联
    body=models.TextField() #String字段
    publish=models.DateTimeField(default=timezone.now) #时间字段，调用timezone包
    
    class Meta: #定义对象的显示顺序：publish对象的倒序顺序显示
        ordering=("-publish",)
        
    def __str__(self):
        return self.title