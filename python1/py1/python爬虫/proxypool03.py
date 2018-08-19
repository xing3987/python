# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 23:11:25 2018

@author: Administrator
"""

'''
定义一个类，用于调用proxypool02中crawl开头的方法，获取抓取到的代理，并存储到数据库
'''

from proxypool01 import RedisClient
from proxypool02 import Crawler

pool_upper=10000

class Getter():
    def __init__(self):
        self.redis=RedisClient()
        self.crawler=Crawler()
        
    def is_over(self):
        #判断是否达到了代理池限制
        if self.redis.count() >= pool_upper:
            return True
        else:
            return False
        
    def run(self):
        print('获取器开始执行')
        if not self.is_over():
            for callback_label in range(self.crawler.__CrawlFuncCount__):
                callback=self.crawler.__CrawlFunc__[callback_label]
                proxies=self.crawler.get_proxies(callback)
                for proxy in proxies:
                    self.redis.add(proxy)
                    
'''
getter=Getter()
getter.run()
'''

'''
定义一个类来检测代理是否可用
'''

















