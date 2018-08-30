# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 22:36:08 2018

@author: Administrator
"""
#爬取微信公众号
from requests import Request

timeout=10

class WeixinRequest(Request):
    def __init__(self,url,callback,method='GET',headers=None,need_proxy=False,fail_time=0,timeout=timeout):
        Request.__init__(self,method,url,headers)
        self.callback=callback
        self.need_proxy=need_proxy
        self.fail_time=fail_time
        self.timeout=timeout
        
'''
实现请求队列Redis的rpush()和lpop()方法,使用pickle模块对request对象序列化
'''
from pickle import dumps,loads
import redis

redis_host='127.0.0.1'
redis_port=6379
redis_password=None
redis_key='weixinRequest'

class RedisQueue():
    def __init__(self):
        self.db=redis.StrictRedis(host=redis_host,port=redis_port,password=redis_password)
        
    def add(self,request):
        if isinstance(request,WeixinRequest):
            return self.db.rpush(redis_key,dumps(request))  #dumps()将对象序列化储存
        return False
    
    def pop(self):
        if self.db.llen(redis_key): #如果该key的长度不为0
            return loads(self.db.lpop(redis_key)) #loads()将对象反序列化
        else:
            return False
        
    def empty(self):
        return self.db.llen(redis_key)==0
 

       
        
















