# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 23:51:41 2018

@author: Administrator
"""

#ajax爬取微博前10页数据并存入mongoDB

from urllib.parse import urlencode  #把param转成url格式
import requests

base_url='https://weibo.com/a/aj/transform/loadingmoreunlogin?'
headers={
        'Host':'weibo.com',
        'Referer':'https://weibo.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
        }


#定义一个函数，传入page和rnd(13位时间参数如:1532274415277)得到返回的ajax的json串
def get_page(page,rnd):  
    params={
            'ajwvr':'6',
            'category':'0',
            'page':page,
            'lefnav':'0',
            'cursor':'',
            '__rnd':rnd
            }
    url=base_url+urlencode(params)
    try:
        response=requests.get(url,headers=headers,timeout=20)
        if response.status_code==200:
           return response.json()
    except requests.ConnectionError as e:
        print('Error',e.args)


#解析得到的数据，生成标题和内容
from pyquery import PyQuery as pq
x=1
def parse_page1(json):
    if json:
        data=json.get('data')
        doc=pq(data)
        context=doc('h3').items()
        weibo={}
        global x
        for a in context:
            x+=1
            weibo['_id']=x  #数据库如果没有‘_id’属性会自动生成，当同时插入多条数据时，会包id相同的错误
            weibo['title']=a.text()
            yield weibo
            
            
#创建方法把数据存入数据库
from pymongo import MongoClient

client=MongoClient(host='localhost',port=27017)
db=client.weibo
collection=db.context
def save_to_mongo(result1):
    if collection.insert(result1):
        print('save to mongo')
  


collection.remove()
#主程序，有十页ajax数据page--1~10
#json1=get_page(1,1532273786141)
#get_page(2,1532273756154)          
#parse_page1(json1)
collection.remove()        
if __name__=='__main__':
    for i in range(1,10):
        j=1532273786141+i
        jsons=get_page(i,j)
        results=parse_page1(jsons)
        for result in results:
            save_to_mongo(result)
                     
texts=collection.find()
for text in texts:
    print(text)
    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

















