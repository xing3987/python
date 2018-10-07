# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
'''
pipelines主要用于对item的操作
实现方法很简单，只要定义一个类，实现process_item()方法就行
'''

'''
筛选text长度大于50的item，并将结果保存到MongoDB
'''
from scrapy.exceptions import DropItem

class ItemPipeline(object):
    def __init__(self):
        self.limit=50
        
    def process_item(self, item, spider):
        if item['text']:
            if len(item['text'])>self.limit:
                item['text']=item['text'][0:self.limit].rstrip()+"..."  #string.strip(s[, chars])，它返回的是字符串的副本，并删除前导和后缀字符。 
                                    #lstrip()和rstrip() 一个是去掉左边的(头部)，一个是去掉右边的(尾部)。
            return item
        else:
            return DropItem('Missing Text') #如果item中text字段不存在，则抛出异常，则该item就会被抛弃，不处理
        

'''
存入数据库,数据库名和url都应该从settings.py配置文件中得到
'''
import pymongo

class MongoPipeline(object):
    def __init__(self,mongo_url,mongo_port,mongo_db):
        self.mongo_url=mongo_url
        self.mongo_port=mongo_port
        self.mongo_db=mongo_db
        
    def open_spider(self,spider):  #spider开启时调用该方法
        self.client=pymongo.MongoClient(self.mongo_url,port=self.mongo_port)
        self.db=self.client[self.mongo_db]
        
    @classmethod     #依赖注入的方式，得到settings.py中的配置信息,参数为crawler
    def from_crawler(cls,crawler):
        return cls(
                mongo_url=crawler.settings.get('MONGO_URL'), #通过crawler参数得到具体的配置信息
                mongo_port=crawler.settings.get('MONGO_PORT'),
                mongo_db=crawler.settings.get('MONGO_DB')
                )
       
    def process_item(self,item,spider):  #主方法
        name=item.__class__.__name__  #得到item的名称
        self.db[name].insert(dict(item)) #将item集合插入数据库
        return item
    
    def close_spider(self,spider): #spider关闭时，关闭数据库
        self.client.close()
        
    
        
    
        

    