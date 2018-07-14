# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 18:47:26 2018

@author: Administrator
"""

import requests


r=requests.get('https://www.baidu.com/')
r.encoding='utf-8'   #解码
print(type(r))
print(r.status_code)
print(r.text)
print(r.cookies)
r.close()

'''
多种请求格式
requests.post()
requests.put()
requests.delete()
requests.head()
requests.options()
'''
print('----------------')

r=requests.get('http://httpbin.org/get')
print(r.text)

data={'name':'Marry','age':'18'}
r=requests.get('http://httpbin.org/get',params=data)
print(r.text) #得到string类型字符串（json格式）
print(r.json) #直接返回json格式字典



r.close()