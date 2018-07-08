# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 23:56:48 2018

@author: Administrator
"""

#data参数,使用该参数，请求类型变成post

import urllib.parse
import urllib.request
import urllib.error
import socket

datas=bytes(urllib.parse.urlencode({'world':'hello'}),encoding='utf8')  #bytes()把字符串转成指定编码格式的字节流类型
response=urllib.request.urlopen('http://httpbin.org/post',data=datas)
print(response.read())

#timeout参数用于设置超时时间，如果超时没有响应会抛出urlError异常,用于控制一个网页长时间未响应，跳过抓取
responseTime=urllib.request.urlopen('http://httpbin.org/get',timeout=1)  
print(responseTime.read())

try:
    responseTime=urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')

'''     
Request类构建完整的请求
class urllib.request.Request(url,data=None,headers={},origin_req_host=None,unverifiable=False,methd=None)
    1.请求路径
    2.bytes字节流数据
    3.请求头
    4.请求方的host或者ip
    5.请求是否可验证
    6.请求方法
'''

url='http://httpbin.org/post'
headers={
        'User-Agent':'Mozlla/4.0(compatible;MSIE 5.5;Windows NT)',
        'Host':'httpbin.org'
        }

dict={'name':'Germey'}

data=bytes(urllib.parse.urlencode(dict),encoding='utf8')
req=urllib.request.Request(url,data,headers,'POST') #或urllib.request.Request(url=url,data=data,headers=headers,'POST')
response=urllib.request.urlopen(req)
print(response.read().decode('utf-8'))










