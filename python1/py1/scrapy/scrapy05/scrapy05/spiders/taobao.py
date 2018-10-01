# -*- coding: utf-8 -*-

'''
对接selenium爬取淘宝数据
'''
import scrapy
from urllib.parse import quote
from pyquery import PyQuery as pq
from scrapy05.items import ProductItem
import time
class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['www.taobao.com,s.taobao.com'] 
    
    def start_requests(self):
        base_urls='https://s.taobao.com/search?q='
        for page in range(1,self.settings.get('MAX_PAGE')+1):
            url=base_urls+quote(self.settings.get('KEYWORDS'))
            print('************'+url+'*****************'+str(page))
            time.sleep(5)
            yield scrapy.Request(url,callback=self.parse,meta={'page':page},dont_filter=True)  #dont_filter设置不去重，meta传递参数给下个函数

    def parse(self, response):
        print('////////start parse///////////')
        doc=pq(response.text)
        products=doc('.grid-item .grid-panel').items()
        for product in products:
            item=ProductItem()
            item['image']=product.find('.img').attr('data-src')
            item['price']=product.find('.price').text()
            item['title']=product.find('.product-title').attr('title')
            item['shop']=product.find('.sale-row .week-sale').text()
            
            print('///////////////////'+item['title'])
            yield item