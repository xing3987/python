# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import time
from scrapyweibo.items import WeiboItem,UserItem,UserRelationItem
class WeiboPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,WeiboItem): #多个item时，使用isinstance来判断是哪个item
            if item.get('created_at'):
                item['created_at']=item['created_at'].strip()
                item['created_at']=self.parse_time(item.get('created_at'))
        return item
    
    def parse_time(self,date):
        #过滤时间,统一成标准时间格式
        if re.match('刚刚',date):
            date=time.strftime('%Y-%m-%d %H:%M',time.localtime(time.time())) #格式化时间为当前时间，time.localtime(time.time())返回当前时间戳(long)
        if re.match('\d+分钟前',date):
            minute=re.match('(\d+)',date).group(1)
            date=time.strftime('%Y-%m-%d %H:%M',time.localtime(time.time()-float(minute)*60))
        if re.match('\d+小时前',date):
            hour=re.match('(\d+)',date).group(1)
            date=time.strftime('%Y-%m-%d %H:%M',time.localtime(time.time()-float(hour)*60*60))
        if re.match('昨天.*',date):
            date=re.match('昨天.*',date).group(1).strip()
            date=time.strftime('%Y-%m-%d',time.localtime()-24*60*60)+' '+date
        if re.match('\d{2}-\d{2}',date):
            date=time.strftime('%Y-',time.localtime())+date+' 00:00'
        return date
    
class TimePipeline(object):
    def process_item(self,item,spider):
        if isinstance(item,UserItem) or isinstance(item,WeiboItem):
            now=time.strftime('%Y-%m-%d %H:%M',time.localtime())
            item['crawled_at']=now
        return item
    
import pymongo 
class MongoPipeline(object):
    def __init__(self,mongo_url,mongo_db):
        self.mongo_url=mongo_url
        self.mongo_db=mongo_db
       
    @classmethod
    def from_crawler(cls,crawler):
        return cls(
                mongo_url=crawler.settings.get('MONGO_URL'),
                mongo_db=crawler.settings.get('MONGO_DB')
                )
        
    def open_spider(self,spider):
        self.client=pymongo.MongoClient(self.mongo_url)
        self.db=self.client[self.mongo_db]
        self.db[UserItem.collection].create_index([('id',pymongo.ASCENDING)])  #以id创建索引，升序排列
        self.db[WeiboItem.collection].create_index([('id',pymongo.ASCENDING)])
        
    def close_spider(self,spider):
        self.client.close()
        
    def process_item(self,item,spider):
        if isinstance(item,UserItem):
            #第一个参数表示查询条件，第二个参数表示爬取对象，$set操作符表示爬到重复的数据可直接更新，同时不会删除已有的字段，第三个参数True表示数据不存在时直接插入
            self.db[item.collection].update({'id':item.get('id')},{'$set':item},True) 
            
        if isinstance(item,WeiboItem):
            #第一个参数表示查询条件，第二个参数表示爬取对象，$set操作符表示爬到重复的数据可直接更新，同时不会删除已有的字段，第三个参数True表示数据不存在时直接插入
            self.db[item.collection].update({'id':item.get('id')},{'$set':item},True)   
            
        if isinstance(item,UserRelationItem):
            self.db[item.collection].update(
                    {'id':item.get('id')},
                    {'$addToSet':
                        {
                            'follows':{'$each':item['follows']},
                            'fans':{'$each':item['fans']}
                        }
                    },True)
        return item
                























