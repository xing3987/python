# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode
from scrapy import Spider,Request
import json
from scrapy03.items import ImageItem 

class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['images.so.com']
    start_urls = ['http://images.so.com/']
    
    def start_requests(self):
        #分析异步请求获取图片的连接
        data={'ch':'photography','listtype':'new','temp':'1'}
        base_url='https://image.so.com/zj?'
        for page in range(1,self.settings.get('MAX_PAGE')+1):
            data['sn']=page*30
            params=urlencode(data)
            url=base_url+params
            yield Request(url,self.parse) #生成请求的url和回调函数

    def parse(self, response):
        result=json.loads(response.text) #的到的数据是json格式
        for image in result.get('list'): #抓取图片的id,标题,链接，缩略图
            item=ImageItem()
            item['id']=image.get('imageid')
            item['url']=image.get('qhimg_url')
            item['title']=image.get('group_title')
            item['thumb']=image.get('qhimg_thumb_url')
            yield item
