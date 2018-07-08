# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 19:25:27 2018

@author: Administrator
"""

def store(a,b,c,d,e):
    print('name is %s,age is %s,sex is %s,email is %s,phone is %s' %(a,b,c,d,e))

store('mary','15','girl','110','119') 
store(a='mary',c='girl',e='19',b='15',d='50')  #也可以不按照顺序，但是要指定参数名和值

def shop(*a):  #不确定参数的个数，*输出时会当元组输出
    print(a)
    
shop('man')
shop('man','girl')

def mark(**a):  ##不确定参数的个数，**输出时会当字典输出
    print(a)

mark(x=1,y=2)

def add(x,y):
    return x+y

params=(1,2)
params1={1,2}
print(add(*params))  #通过*把值传递到函数中
print(add(*params1))

'''
一些函数案例
'''

def story(**kwds):
    return ('Once upon a time,there was a %(job)s called %(name)s .' %kwds)

print(story(name='gumby',job='king'))
par={'job':'language','name':'python'}
print(story(**par))

def power(x,y,*others):
    if others:
        print('recdived redundant paraneers:',others)
    return pow(x,y)

print(power(2,3))
print(power(2,3,4,5))

def interval(start,stop=None,step=1):
    if stop is None:
        start,stop=0,start
    result=[]
    i=start
    while i<stop:
        result.append(i)
        i+=step
    return result

print(interval(2,step=1))
print(interval(5))   
print(interval(1,8,2))
print(power(*interval(3,8)))     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    