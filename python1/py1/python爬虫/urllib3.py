# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 22:26:47 2018

@author: Administrator
"""

'''
有些网址打开时会弹出提示框，直接提示输入用户名和密码，验证成功后才能查看页面
例：
    url=http://localhost:5000
    username='username'
    password='password'
'''

from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
from urllib.error import URLError

url='https://www.baidu.com'
username='username'
password='password'
p=HTTPPasswordMgrWithDefaultRealm() #实例化对象
p.add_password(None,url,username,password) #添加url和用户密码
auth_handler=HTTPBasicAuthHandler(p)  #实例化handler对象
opener=build_opener(auth_handler)   #实例化opener对象
try:
    result=opener.open(url) #调用opener方法open
    html=result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)