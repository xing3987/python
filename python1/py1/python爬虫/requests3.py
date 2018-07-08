# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 17:34:19 2018

@author: Administrator
"""

#处理post请求
import requests

data={'name':'Jams','age':'18'}
r=requests.post('http://httpbin.org/post',data)
exit() if not r.status_code==requests.codes.ok else print('Request Successfully')
print(r.text)

print('url:',r.url)
print('statusCode:',r.status_code)
print('headers:',r.headers)
print('cookies:',r.cookies)
print('history:',r.history)