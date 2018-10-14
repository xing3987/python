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
    description=scrapy.Field()
    gender=scrapy.Field()
    follows_count=scrapy.Field()
    fans_count=scrapy.Field()
    weibos_count=scrapy.Field()
    
class UserRelationItem(scrapy.Item):
    collection='user_relation'
    id=scrapy.Field()
    follows=scrapy.Field()
    fans=scrapy.Field()

    
class WeiboItem(scrapy.Item):
    collection='weibo'

