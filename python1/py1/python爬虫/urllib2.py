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