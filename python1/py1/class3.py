# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 22:53:05 2018

@author: Administrator
"""


class User:
    pass

if __name__=='__main__':
    print(dir(User()))  #打印输出类中所有的内置方法(魔法方法)'__xx__'

class student:
    def __new__(cls,name,age):  #构造方法
        print('调用了new方法,创建了一个对象')
        return super(student,cls).__new__(cls) #返回父类的方法
    def __init__(self,name,age): #初始化方法
        print('调用了init方法')
        self.name=name
        self.age=age

stu1=student("lily",18)  #创建对象时先调用new方法，后调用init方法
print(stu1.age,stu1.name)

class People:
    def __getattr__(self,name):
        print('调用了_getattr_方法')
        return super(People,self)._getattr__(name)  #注意赋值方式，self.name=name会出现递归效应，又会调用自身的其他魔法方法，不可取
    def __setattr__(self,name,value):
        print('调用了_setarrt_方法')
        return super(People,self).__setattr__(name,value)
    def __delattr__(self,name):
        print('调用了_delattr_方法')
        return super(People,self).__delattr__(name)
    def __getattribute__(self,name):
        print('调用了_getattribute_方法')
        return super(People,self).__getattribute__(name)
    
    
if __name__=='__main__':
    people=People()
    people.attr1=True  #给对象赋值，调用setattr方法
    try:
        people.attr1  #获取有值的对象，调用getattribute方法
        people.attr2  #获取没有赋值的对象，先调用getattribute方法，再调用getattr方法
    except:
       pass
    
    del people.attr1  #删除对象会调用delattr方法
    
 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        