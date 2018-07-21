# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 22:53:37 2018

@author: Administrator
"""

from redis import StrictRedis

redis=StrictRedis(host='localhost',port=6379,db=0) #有password可以在后面加这个参数

#redis是键对形式存在的数据库
redis.set('name','Bob')
print(redis.get('name'))

#使用ConnectionPool连接池连接
from redis import ConnectionPool

pool=ConnectionPool(host='localhost',port=6379,db=0)
redis=StrictRedis(connection_pool=pool)
print(redis.get('name'))
'''
ConnectionPool支持URL构建
redis://[:password]@host:port/db  
rediss://[:password]@host:port/db
unix://[:password]@/path/to/socket.sock?db=db
'''
url='redis://localhost:6379/0'  #无密码时不加password参数,有密码时：'redis://:密码@localhost:6379/0'
pool=ConnectionPool.from_url(url)
redis=StrictRedis(connection_pool=pool)
print(redis.get('name'))

redis.set('name','Bob')
redis.set('age',15)
redis.set('email','119')
redis.set('tel','110')
redis.set('sex','girl')
print(redis.exists('name')) #是否存在该键
print(redis.type('name')) #类型
print(redis.delete('name')) #删除
print(redis.randomkey()) #获得一个随机的键
print(redis.keys()) #获得所有键
print(redis.keys('a*')) #获得a开头的键
print(redis.rename('sex','sexes')) #给键重命名