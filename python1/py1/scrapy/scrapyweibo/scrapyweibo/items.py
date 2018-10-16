# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UserItem(scrapy.Item):   
    collection='users'
    id=scrapy.Field()
    name=scrapy.Field()
    avatar=scrapy.Field()
    cover=scrapy.Field()
    description=scrapy.Field() #自我简述
    gender=scrapy.Field() #性别
    follows_count=scrapy.Field() #关注数量
    fans_count=scrapy.Field() #粉丝数量
    weibos_count=scrapy.Field()
    follows=scrapy.Field() #关注的人
    fans=scrapy.Field() #粉丝
    crawled_at=scrapy.Field()  #爬取的时间
    
#保存对应关系的item最终数据会储存入userItem
class UserRelationItem(scrapy.Item):
    collection='users'
    id=scrapy.Field()
    follows=scrapy.Field()
    fans=scrapy.Field()

    
class WeiboItem(scrapy.Item):
    collection='weibo'
    id=scrapy.Field()
    attitudes_count=scrapy.Field()  #关注
    comments_count=scrapy.Field()  #评论
    reposts_count=scrapy.Field()  #转发
    picture=scrapy.Field()
    pictures=scrapy.Field()
    source=scrapy.Field() #资源
    text=scrapy.Field()  #文字
    raw_text=scrapy.Field()
    thumbnail=scrapy.Field() #小图片
    user=scrapy.Field()
    created_at=scrapy.Field()  #创建时间
    crawled_at=scrapy.Field()  #爬取的时间


