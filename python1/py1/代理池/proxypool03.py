# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 23:11:25 2018

@author: Administrator
"""

from proxypool01 import RedisClient
from proxypool02 import Crawler

test_url='https://m.weibo.cn'
pool_upper=10000

class Getter():
    def __init__(self):
        self.redis=RedisClient()
        self.crawler=Crawler()
        
    def is_over(self):
        if self.redis.count() >= pool_upper:
            return True
        else:
            return False
        
    def run(self):
        if not self.is_over():
            for callback_label in range(self.crawler.__CrawlFuncCount__):
                callback=self.crawler.__CrawlFunc__[callback_label]
                proxies=self.crawler.get_proxies(callback)
                for proxy in proxies:
                    self.redis.add(proxy)
                    

import asyncio 
import aiohttp
import time

status_code=[200]
batch_size=300

class Tester(object):
    def __init__(self):
        self.redis=RedisClient()
        
    async def test_one_proxy(self,proxy):
        conn=aiohttp.TCPConnector(verify_ssl=False) 
        async with aiohttp.ClientSession(connector=conn) as session: 
            try:
                if isinstance(proxy,bytes):
                    proxy=proxy.decode('utf-8')
                real_proxy='http://'+proxy
                async with session.get(test_url,proxy=real_proxy,timeout=15) as response:
                    if response.status in status_code:
                        self.redis.max(proxy)
                    else:
                        self.redis.decrease(proxy)
            except:
                self.redis.decrease(proxy)
                print('false:',proxy)
                
    def run(self):
        try:
            proxies=self.redis.all()
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop) 
            for i in range(0,len(proxies),batch_size):
                test_proxies=proxies[i:i+batch_size]
                tasks=[self.test_one_proxy(proxy) for proxy in test_proxies]
                loop.run_until_complete(asyncio.wait(tasks)) 
                time.sleep(5)
        except Exception as e:
            print('except:',e.args)













