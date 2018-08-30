# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 00:01:14 2018

@author: Administrator
"""

'''
构造第一个请求放到队列里以供调度
'''
from requests import Session
from weixin01 import RedisQueue,WeixinRequest
from urllib.parse import urlencode

class SpiderWxpq():
    base_url="http://weixin.sogou.com/weixin"
    keyword='101女团'
    headers={
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Connection':'keep-alive',
            'Cookie':'ABTEST=8|1535294251|v1; IPLOC=CN3205; SUID=25DD25993E18960A000000005B82BB2B; __guid=14337457.825266257461256600.1535294197572.036; SUID=25DD25992B12960A000000005B82BB2B; weixinIndexVisited=1; SUV=008D64129925DD255B82BB3C73FBF439; SNUID=39C038841D19694B936161FF1DCB7ADA; JSESSIONID=aaaSAbCTCtOlqh10h6Bvw; monitor_count=35; sct=5',
            'Host':'weixin.sogou.com',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
            }
    session=Session()
    queue=RedisQueue()
    
    def start(self):
        #初始化
        self.session.headers.update(self.headers)
        start_url=self.base.url+'?'+urlencode({'type':2,'s_from':'input','query':self.keyword})
        weixin_request=WeixinRequest(url=start_url,callback=self.parse_index,need_proxy=True)
        #调度一个请求
        self.queue.add(weixin_request)
        
    
    
    
    
    
    
    
    
    
