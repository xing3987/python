# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 22:45:03 2018

@author: Administrator
"""
from math import pi
print(pi)
print('%3.12f' %pi)  #打印浮点数，默认长度为3位(如果小数位大于长度，自动扩长)，小数位为12位
print('%.5s' %('hello world!')) #格式化字符串，保留5位
print('%.*s' %(5,'hello world!')) #也可以先用*号代替长度，后面给长度赋值
print('%010.5f' %pi) #长度为10位，不足补0（也可以为空格或者加减号）

num=['a','b','c']
print('/'.join(num)) #split的逆方法，用来插入连接字符串的符号

print("asdfasdfasdfa".find('d'))  #查找字符串中的数字
print("Jasdfasdf".replace('a','xx')) #查找，并把找到的替换
print('          aa              '.strip()) #去除两端空字符