# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 00:04:16 2018

@author: Administrator
"""
'''
定义一个类，用来管理redis的连接池
'''
max_score=100
min_score=0
initial_score=10
redis_host='localhost'
redis_port=6379
redis_password=None
redis_key='proxies'



import redis
from random import choice


#print(choice([1,2,3,54,3])) #random.choice(seq)方法返回一个列表，元组或字符串的随机项。

class RedisClient(object):
    def __init__(self,host=redis_host,port=redis_port,password=redis_password): 
        #初始化连接redis
        self.db=redis.StrictRedis(host=host,port=port,password=password,decode_responses=True)
        
    def add(self,proxy,score=initial_score):
        #添加代理，并设定初始化分数
        if not self.db.zscore(redis_key,proxy): #zscore(redis_key,proxy)查询redis_key键中proxy的值，如果为空返回null
            return self.db.zadd(redis_key,score,proxy) #proxy不为空时，初始化proxy的值，zdd（）给有序集合的键中加值(可以加多个)
        
    def random(self):
        #随机获取有效代理
        result=self.db.zrangebyscore(redis_key,max_score,max_score) #zrangebyscore(key,a,b)返回key键中score的值a到b大小的所有元素
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
        #代理不可用时，分数减一，小于最小值删除
        score=self.db.zscore(redis_key,proxy)
        if score and score>min_score:
            print('代理',proxy,'当前分数',score,'减一')
            return self.db.zincrby(redis_key,proxy,-1) #zincrby(key,member,value)使key键成员member数组减一
        else:
            print('代理',proxy,'当前分数',score,'删除')
            return self.db.zrem(redis_key,proxy)
        
    def exits(self,proxy):
        #判断代理是否存在
        return not self.db.zscore(redis_key,proxy)==None
    
    def max(self,proxy):
        #代理可以使用时，将代理设置成最大数值
        print('代理',proxy,'可用，设置为',max_score)
        return self.db.zadd(redis_key,max_score,proxy)  #zadd()更新或者添加变量
    
    def count(self):
        #获取代理数量
        return self.db.zcard(redis_key)
        
    def all(self):
        return self.db.zrangebyscore(redis_key,min_score,max_score)
        
        
        
        
        
        
        
        
        
        