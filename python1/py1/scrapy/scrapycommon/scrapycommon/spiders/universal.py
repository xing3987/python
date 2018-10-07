# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapycommon.utils import get_config
from scrapycommon.configs.rules import rules
from scrapycommon.items import NewsItem
from scrapycommon  import utils 

class UniversalSpider(CrawlSpider):
    name = 'universal'

    def __init__(self,name,*args,**kwargs):
        config=get_config(name)
        self.config=config
        self.rules=rules.get(config.get('rules'))
        start_urls=config.get('start_urls')
        if start_urls:  #实现url的动态配置
            if start_urls.get('type')=='static':
                self.start_urls=start_urls.get('value')
            elif start_urls.get('type')=='dynamic':
                self.start_urls=list(eval('utils.'+start_urls.get('method'))(*start_urls.get('args',[]))) #配置文件方法在utils中，和json的start_urls方法名对应
        
        self.allowed_domains=config.get('allowed_domains')
        super(UniversalSpider,self).__init__(*args,**kwargs) #继承父类的传参

    def parse_item(self, response):
        item=self.config.get("item")
        if item:
            cls=eval(item.get('class'))()  #eval() 函数用来执行一个字符串表达式，并返回表达式的值。即：cls=NewsItem()
            loader=eval(item.get('loader'))(cls,response=response) #即：loader=ChinaLoader(item = NewsItem(),response=response)
            #动态获取配置
            for key,value in item.get('attrs').items():  #.items()把得到的结果赋值成item，从而得到key,value
                for extractor in value:
                    if extractor.get('method')=='xpath':
                        loader.add_xpath(key,*extractor.get('args'),**{'re':extractor.get('re')})
                    if extractor.get('method')=='css':
                        loader.add_css(key,*extractor.get('args'),**{'re':extractor.get('re')})
                    if extractor.get('method')=='value':
                        loader.add_value(key,*extractor.get('args'),**{'re':extractor.get('re')})
                    if extractor.get('method')=='attr':
                        loader.add_value(key,getattr(response,*extractor.get('args')))
            yield loader.load_item()
            




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
