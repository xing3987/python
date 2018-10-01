# -*- coding: utf-8 -*-
import scrapy
from scrapy04.items import ImagesItem
import re

class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['1024.hlork9.club','p5.urlpic.club']
    start_urls = ['http://1024.hlork9.club/pw/thread.php?fid=21']
    
    def parse_detail(self,response):      
        #编写正则表达式:需要提取
        pattern=re.compile('<img src="http(.*?)" border="0" onclick=.*?>',re.S)
        itemurls=re.findall(pattern,response.text)
        for itemurl in itemurls:
            url="http"+itemurl
            print(url)
            item=ImagesItem()
            item['url']=url
            yield item
  
    def parse(self, response):
        base_url='http://1024.hlork9.club/pw/'
        pageurls=response.xpath('//tr[@class="tr3 t_one"]/td/a/@href').extract()
        for pageurl in pageurls:            
            url=base_url+pageurl
            print('*****'+url)
            yield scrapy.Request(url=url,callback=self.parse_detail)
            

            
        
