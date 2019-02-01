from django.contrib import admin
from .models import BlogArticles
from account.models import UserInfo
# Register your models here.
class BlogArticlesAdmin(admin.ModelAdmin):
    list_display=("title","author",'publish')
    list_filter=('publish','author')
    search_fields=('title','body')
    raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering=['publish','author']

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ("user","school","company","profession","address","aboutme","photo")
    list_filter=('school','company',"profession")

admin.site.register(UserInfo,UserInfoAdmin) #将实体类引入当前环境,然后注册到admin中
admin.site.register(BlogArticles,BlogArticlesAdmin)