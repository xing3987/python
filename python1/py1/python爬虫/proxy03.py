# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 22:37:33 2018

@author: Administrator
"""

'''
requests代理设置
'''    
import requests

proxy='127.0.0.1:80'
proxies={
        'http':'http://'+proxy,
        'https':'https://'+proxy
        }
try:
    response=requests.get('http://httpbin.org/get',proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error',e.args)
    
    
'''
socks5代理
'''
proxy='127.0.0.1:80'
proxies={
        'http':'socks5://'+proxy,
        'https':'socks5://'+proxy
        }
#其它同普通requests
    