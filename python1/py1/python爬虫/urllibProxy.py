# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 22:43:10 2018

@author: Administrator
"""

#使用代理连接服务器
from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener
#import urllib.request

proxy_handler=ProxyHandler({
        'http':'http://127.0.0.1:8888',
        'https':'https://127.0.0.1:8888'
        })

opener=build_opener(proxy_handler)
try:
    response=opener.open('https://www.github.com')
    #response=urllib.request.urlopen('https://www.baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)