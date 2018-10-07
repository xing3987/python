# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 23:12:36 2018

@author: Administrator
"""
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
rules={
       "china":(
               #allow指定了匹配的正则表达式，restrict_xpaths指定了匹配的范围.根据规则自动生成了匹配到的request
        Rule(LinkExtractor(allow=r'article\/.*?\.html',restrict_xpaths='//div[@id="left_side"]//div[@class="con_item"]'), callback='parse_item'),
            #Rule会自动提取超链接
        Rule(LinkExtractor(restrict_xpaths='//div[@id="pageStyle"]//a[contains(.,"下一页")]'))
 
               )
       }