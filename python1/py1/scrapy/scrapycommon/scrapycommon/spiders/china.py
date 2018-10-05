# -*- coding: utf-8 -*-

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapycommon.items import NewsItem

class ChinaSpider(CrawlSpider):
    name = 'china'
    allowed_domains = ['tech.china.com']
    start_urls = ['http://tech.china.com/articles/']

    rules = (
            #allow指定了匹配的正则表达式，restrict_xpaths指定了匹配的范围.根据规则自动生成了匹配到的request
        Rule(LinkExtractor(allow=r'article\/.*?\.html',restrict_xpaths='//div[@id="left_side"]//div[@class="con_item"]'), callback='parse_item'),
        #Rule会自动提取超链接
        Rule(LinkExtractor(restrict_xpaths='//div[@id="pageStyle"]//a[contains(.,"下一页")]'))
    )
    
    #使用loader改进代码
    def parse_item(self, response):
        loader=ChinaLoader(item = NewsItem(),response=response)
        loader.add_xpath('title','//h1[@id="chan_newsTitle"]/text()')
        loader.add_value('url',response.url)
        loader.add_xpath('text','//div[@id="chan_newsDetail"]//p/text()')
        loader.add_xpath('datetime','//div[@id="chan_newsInfo"]/text()',re='(\d+-\d+-\d+\s\d+:\d+:\d+)')
        loader.add_xpath('source','//div[@id="chan_newsInfo"]/text()',re='来源：(.*)')
        loader.add_value('website','中华网')
        yield loader.load_item()

'''
    def parse_item(self, response):
        item = NewsItem()
        item['title'] = response.xpath('//h1[@id="chan_newsTitle"]/text()').extract_first()
        item['url'] = response.url
        item['text'] =''.join(response.xpath('//div[@id="chan_newsDetail"]//p/text()').extract()).strip()
        item['datetime'] = response.xpath('//div[@id="chan_newsInfo"]/text()').re_first('(\d+-\d+-\d+\s\d+:\d+:\d+)')  #得到第一个正则匹配的数
        item['source'] = response.xpath('//div[@id="chan_newsInfo"]/text()').re_first('来源：(.*)').strip()
        item['website'] = '中华网'
        yield item
'''

'''
改进代码，使提取方式更规整
'''
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst,Join,Compose

#TakeFirst用来取得第一个符合的条件，效果类似extract_first()
#Join()可以把列表拼合成字符串
#Compose用来指定运行的方法

class NewsLoader(ItemLoader):
    default_output_processors=TakeFirst()  #指定默认输出
    
class ChinaLoader(NewsLoader):
    text_out=Compose(Join(),lambda s:s.strip()) #lambda s:s.strip(),匿名函数用来去除头尾空格
    source_out=Compose(Join(),lambda s:s.strip())