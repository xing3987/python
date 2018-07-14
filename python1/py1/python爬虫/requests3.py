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
print('---------------------')
#文件上传
files={'file':open('favicon.ico','rb')}
r=requests.post('http://httpbin.org/post',files=files)  #不写files=files默认files是在form里post,写了会单独在files里发送
print(r.text)

r=requests.get('https://www.baidu.com')
print(r.cookies)
for key,value in r.cookies.items(): #输出cookies
    print(key,value)
    

print('--------------------------')    
'''
模拟登陆github
1.首先手动登陆github,得到cookies和host,user-agent(打开调试-network，然后刷新页面)
'''

headers={
        'Cookie':'_octo=GH1.1.504639994.1531043286; logged_in=yes; dotcom_user=xing3987; _gat=1; _ga=GA1.2.1984624114.1531043286',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        }

r=requests.get('https://github.com',headers=headers)
print(r.text)
print('--------------------------') 

r.close()












