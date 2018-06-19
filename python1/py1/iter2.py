# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 22:39:37 2018

@author: Administrator
"""

def fun():
    for i in range(10):
        print(i)
        
fun()


'''
创建生成器，把print变成yield
'''
def fun1():
    for i in range(10):
        yield(i)
        
        
print(fun1())

def fibon(n):
    a=b=1
    for i in range(n):
        yield a
        a,b=b,a+b
        
for x in fibon(10):
    print(x,end='')