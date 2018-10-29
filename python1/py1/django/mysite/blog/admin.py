from django.contrib import admin
from .models import BlogArticles
# Register your models here.



class BlogArticlesAdmin(admin.ModelAdmin):
    list_display=("title","author",'publish')
    list_filter=('publish','author')
    search_fields=('title','body')
    raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering=['publish','author']
    
    
    
    
    
    
    
admin.site.register(BlogArticles,BlogArticlesAdmin) #将实体类引入当前环境,然后注册到admin中