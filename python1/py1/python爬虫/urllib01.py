# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 22:54:16 2018

@author: Administrator

"""
#爬去python官网页面
import urllib.request

response=urllib.request.urlopen('https://www.python.org')
print(response.read().decode('utf-8'))

print(type(response))
print(response.status)
print(response.getheaders())