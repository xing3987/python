# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 22:55:34 2018

@author: Administrator
"""

print(bool('hello')) #判断true or false
print(bool(0)) #0 或''为false

name=input('what is your name?')
if name.endswith("lily"):
    if name.startswith('mr'):
        print('hello my boy %s' %name)
    elif name.startswith("mrs"):
        print('hello my lady %s' %name)
    else:
        print('hello %s' %name)
else:
    print('hello stranger')
  
'''    
python 中可以用0<a<100这样判断数字
        x is not y
        x not in y
        x is y等...
'''
age=55
if 0<age<100:
    print('It is a num in 100')
    
    
x=y=[1,2,3]
z=[1,2,3]
print(x==z)
print(x is z)   #判断是不是同一个对象 

x=1
while x<100:
    print('%d小于100' %x)
    x+=10
 
for num in z:
    print(num)
    
print(range(10)) #range生成0~目标数的整数元组    
for num in range(10):
    print(num)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    