# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 22:40:37 2018

@author: Administrator
"""

print(1,2,3) #print可以用逗号隔开，但是输出会有空格
print('a','1',3)
print('a'+'b'+'3')

student={'name':'mary','age':'18'}
key,value=student.popitem(); #去一对键值，并赋给key,value
print(key,value)
hello,man=1,2;
print(hello)

x='aaa'
y=12
print(x,y)
print(x+'%d' %y) #使用这个方式连接字符串和数字
print(x+str(y))  #使用str()把数字转换成字符串