# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 16:07:04 2018

@author: Administrator
"""

try:
    x=input('Enter the first number:')
    y=input('Enter the second number:')
    print(x/y)
except TypeError:  #多个异常用()号写一起，也可以用通用异常BaseException或者后面什么都不写
    print("that  wasn't a number,was it?")
    
while True:
    try:   
        x=int(input('Enter the first number:'))
        y=int(input('Enter the second number:'))
        print(x/y)
    except TypeError:  #多个异常用()号写一起，也可以用通用异常BaseException或者后面什么都不写
        print("that  wasn't a number,was it?")
        print('please try again')
    else:
        break