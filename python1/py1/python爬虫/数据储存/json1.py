# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 23:12:01 2018

@author: Administrator
"""
'''
json数据必须要用{}大括号包裹，并且用“”双引号和：冒号赋值
'''
import json

str1='''[{"name":"bob","gender":"male","birthday":"1992-10-18"}]'''

print(type(str1))
data=json.loads(str1)
print(type(data))

#读取json对象
print(data[0]["name"])
print(data[0].get('name')) #两种方法都可以取值
print(data[0].get('number')) #当没有对应的键值为null
print(data[0].get('number',2))  #get的第二个参数是默认值

#写入文件.json格式

with open('jsondata.json','w') as file:
    #file.write(json.dumps(data))  #dumps把json对象转成数组
    file.write(json.dumps(data,indent=2)) #indent代表缩进字符个数
    
#读取json文件   
with open('jsondata.json','r') as file:
    str2=file.read()
    data=json.loads(str2)
    print(data)
    
#当有中文时，json的读写，默认是输出Unicode字符，需要转码    
str2='''[{"name":"王五","gender":"人妖","birthday":"1992-10-18"}]'''

with open('jsondata.json','a',encoding='utf-8') as file:  #设置好文本的格式
    data=json.loads(str2)
    file.write(json.dumps(data,indent=2,ensure_ascii=False)) #ensure_ascii设置取消默认转码
