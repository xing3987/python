# -*- coding: utf-8 -*-
import scrapy
from scrapy01.items import QuoteItem 

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes=response.css('.quote')
        for quote in quotes:
            item=QuoteItem()
            item['text']=quote.css('.text::text').extract_first()
            item['author']=quote.css('.author::text').extract_first()
            item['tags']=quote.css('.tags .tag::text').extract()
            yield item
            
        next=response.css('.pager .next a::attr("href")').extract_first()
        url=response.urljoin(next)   #urljoin() 加入到当前路径后一起返回
        yield scrapy.Request(url=url,callback=self.parse)
