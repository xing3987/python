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

#定义测试的url
test_url='https://m.weibo.cn'
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
定义一个类来检测代理是否可用,使用异步代理请求库aiohttp
'''
import asyncio 
import aiohttp
import time

status_code=[200]
batch_size=300

class Tester(object):
    def __init__(self):
        self.redis=RedisClient()
        
    async def test_one_proxy(self,proxy):
        #测试单个proxy
        conn=aiohttp.TCPConnector(verify_ssl=False) #创建连接
        async with aiohttp.ClientSession(connector=conn) as session:  #async异步请求关键词
            try:
                if isinstance(proxy,bytes):
                    proxy=proxy.decode('utf-8')
                real_proxy='http://'+proxy
                print('正在测试',proxy)
                async with session.get(test_url,proxy=real_proxy,timeout=15) as response:
                    if response.status in status_code:
                        self.redis.max(proxy)
                        print('代理可用',proxy)
                    else:
                        self.redis.decrease(proxy)
                        print('请求响应码不合法',proxy)
            except:
                self.redis.decrease(proxy)
                print('代理请求失败',proxy)
                
    def run(self):
        #测试主函数
        print('测试器开始运行')
        try:
            proxies=self.redis.all()
            #loop=asyncio.get_event_loop()  #创建连接池
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop) #创建新的loop可以避免loop冲突异常
            for i in range(0,len(proxies),batch_size):
                test_proxies=proxies[i:i+batch_size]
                tasks=[self.test_one_proxy(proxy) for proxy in test_proxies]
                loop.run_until_complete(asyncio.wait(tasks)) #启动连接池
                time.sleep(5)
        except Exception as e:
            print('测试器发生异常',e.args)













