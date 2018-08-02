# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 21:35:13 2018

@author: Administrator
"""
'''
本地docker先起一个splash服务器端口ip:192.168.99.100:8050
'''
import requests

url="http://192.168.99.100:8050/render.png?url=https://www.jd.com&wait=5&width=1000&height=700"
response=requests.get(url)
with open("image/jingdong.png","wb") as f:
    f.write(response.content)
    
    
'''
使用splash脚本lua语言
'''

lua='''
function main(splash)
    return 'hello'
end
'''

from urllib.parse import quote  #使用quote对url进行转码
url='http://192.168.99.100:8050/execute?lua_source='+quote(lua)
response=requests.get(url)
print(response.text)

lua1='''
function main(splash,args)
    local treat=require('treat')
    local response=splash:http_get('http://httpbin.org/get')
        return{
                html=treat.as_string(response.body),
                url=response.url,
                status=response.status
        }
end
'''
url='http://192.168.99.100:8050/execute?lua_source='+quote(lua1)
response=requests.get(url)
print(response.text)