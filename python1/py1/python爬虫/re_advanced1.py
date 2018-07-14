# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 23:01:18 2018

@author: Administrator
"""

import re

#match从头开始匹配
print('----match---')
content='Hello 123 4567 World_this is a Regex Demo'
result=re.match('Hello\s\d{3}\s\d{3,6}\s\w{10}',content)
print(result)
print(result.group())
print(result.span()) #输出匹配过的位置，范围

#使用()来取得匹配中需要的字段
print('----(分组)---')
result=re.match('Hello\s\d{3}\s(\d{3,6})\s\w{10}',content)
print(result.group(0)) #group(0)表示匹配到的字符
print(result.group(1))  #第一个括号中的目标字符
print(result.span())

#使用通配符.*
print('---通配符----')
result=re.match('Hello.*Demo',content)
print(result.group())

#贪婪与非贪婪?
print('----贪婪与非贪婪---')
result=re.match('Hello.*(\d+)\s\w{10}',content)
print(result.group(1))  #.*是贪婪的，它会尽量多的匹配

result=re.match('Hello.*?(\d+)\s\w{10}',content)
print(result.group(1))  #.*?是非贪婪的，它会尽量少的匹配


#当目标字段中有换行符时需要用到修饰符
print('----修饰符---')
content='Hello 123 4567 World_this'+'\n'+' is a Regex Demo'
print(content)
result=re.match('Hello.*Demo',content,re.S) #不使用re.S会匹配不到，报错
print(result.group())

#search()可以不用从头开始匹配,返回第一个符合条件的数据，这个最常用
print('----常用匹配方法search---')
result=re.search('123.*Demo',content,re.S)
print(result.group())
























