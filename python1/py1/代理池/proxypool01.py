# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 00:04:16 2018

@author: Administrator
"""

max_score=100
min_score=0
initial_score=10
redis_host='192.168.1.100'
redis_port=6379
redis_password=None
redis_key='proxies'


import redis
from random import choice

class RedisClient(object):
    def __init__(self,host=redis_host,port=redis_port,password=redis_password): 
        self.db=redis.StrictRedis(host=host,port=port,password=password,decode_responses=True)
        
    def add(self,proxy,score=initial_score):
        if not self.db.zscore(redis_key,proxy): 
            return self.db.zadd(redis_key,score,proxy)
        
    def random(self):
        result=self.db.zrangebyscore(redis_key,max_score,max_score)
        if len(result):
            print(result)
            return choice(result)
        else:
            result=self.db.zrevrange(redis_key,0,100)
            if len(result):
                return choice(result)
            else:
                raise Exception("pool is empty")
        
    def decrease(self,proxy):
        score=self.db.zscore(redis_key,proxy)
        if score and score>min_score:
            print('代理',proxy,'当前分数',score,'减一')
            return self.db.zincrby(redis_key,proxy,-1) 
        else:
            print('代理',proxy,'当前分数',score,'删除')
            return self.db.zrem(redis_key,proxy)
        
    def exits(self,proxy):
        return not self.db.zscore(redis_key,proxy)==None
    
    def max(self,proxy):
        print('代理',proxy,'可用，设置为',max_score)
        return self.db.zadd(redis_key,max_score,proxy)  
    
    def count(self):
        return self.db.zcard(redis_key)
        
    def all(self):
        return self.db.zrangebyscore(redis_key,min_score,max_score)
        
        
        
        
        
        
        
        
        
        