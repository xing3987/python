# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 23:11:30 2018

@author: Administrator
"""
'''
对象的描述器obj/instance
'''

class User:
    def __init__(self,name='mary',sex='boy'):
        self.name=name
        self.sex=sex
    def __get__(self,obj,objtype):
        print('获取name值')
        return self.name
    def __set__(self,obj,val):
        print('设置name值')
        self.name=val
        
        
        
class MyClass:
    x=User('tom','boy')
    y=5
    
if __name__=='__main__':
    m=MyClass()
    print(m.x,m.y)
    
    m.x='mary'
    print(m.x)

class Meter:
    def __int__(self,value=0.0):
        self.value=float(value)
    def __get__(self,instance,owner):
        return self.value
    def __set__(self,instance,value):
        self.value=float(value)
        
class Foot:
    def __get___(self,instance,owner):
        return instance.meter*3.2808
    def __set__(self,instance,value):
        instance.meter=float(value)/3.2808
        
class Distance:
    meter=Meter()
    foot=Foot()
    
if __name__=='__main__':
    d=Distance()
    print(d.meter,d.foot)
    d.meter=1
    print(d.meter,d.foot)
    d.meter=2
    print(d.meter,d.foot)
    
    
    
    
    
    
    
    
    
    
    