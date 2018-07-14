# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 23:34:41 2018

@author: Administrator
"""
import requests
import urllib3
#session会话技术
requests.get('http://httpbin.org/cookies/set/number/12345')
r=requests.get('http://httpbin.org/cookies')
print(r.text)

    
    
s=requests.Session()
s.get('http://httpbin.org/cookies/set/number/12345')
r=s.get('http://httpbin.org/cookies')
print(r.text)


#SSL证书验证
'''
rs=requests.get('https://www.12306.cn')
print(rs.status_code)  #运行出现ssl错误
'''
urllib3.disable_warnings() #忽略警告
rs=requests.get('https://www.12306.cn',verify=False)  #verify设置成False跳过验证
print(rs.status_code)

'''
#某些网址大规模爬取时需要设置代理

proxies={
        'http':'http://127.0.0.1:3128',
        'https':'http://127.0.0.1:1080'      
        }
#模拟的代理是无效的，所以连接不上
#r=requests.get('https://taobao.com',proxies=proxies)
#print(r.status_code)
'''

#超时设置timeout,连接超时抛出异常,如果设置为None则会一直等待
r=requests.get('https://taobao.com',timeout=1)
print(r.status_code)

'''
#某些网址要添加身份认证
from requests.auth import HTTPBasicAuth

r=requests.get('http://localhost:5000',auth=HTTPBasicAuth('username','password'))
'''

#Prepared Request(把请求变成独立对象)
from requests import Request,Session
url='http://httpbin.org/post'
data={'name':'Marry'}
headers={}
s=Session()
req=Request('POST',url,data=data,headers=headers)
prepped=s.prepare_request(req)
r=s.send(prepped)
print(r.text)
s.close()


r.close()






