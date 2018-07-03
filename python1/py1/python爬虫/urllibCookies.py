# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 23:01:14 2018

@author: Administrator
"""

import http.cookiejar,urllib.request

cookie=http.cookiejar.CookieJar() #声明cookie对象
handler=urllib.request.HTTPCookieProcessor(cookie) #创建一个handler
opener=urllib.request.build_opener(handler) #构建出opener
response=opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name+'='+item.value)
    
#把cookies生成成文件
filename='cookies.txt'
#cookie=http.cookiejar.MozillaCookieJar(filename) #将Cookies保存成Mozilla型的浏览器的Cookies格式
cookie=http.cookiejar.LWPCookieJar(filename) #将Cookies保存成LWP型的浏览器的Cookies格式
handler=urllib.request.HTTPCookieProcessor(cookie) #创建一个handler
opener=urllib.request.build_opener(handler) #构建出opener
response=opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)