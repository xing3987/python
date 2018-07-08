# -*- coding: utf-8 -*-
"""
Created on Wed May  2 21:26:41 2018

@author: Administrator
"""

#函数的定义
def MaxNum(a,b):
    if a>b:
        return a
    elif a<=b:
        return b

print(MaxNum(3,50))

#定义一个函数输出多个变量
def showMe(name,place):
    print('my name is %s I am from %s' %(name,place))
    print('hello world!')
  
name="玛丽"
place="北京"
showMe(name,place)
name="汤姆"
place="南京"
showMe(name,place)

#面向对象思想,定义初始方法注意是两个下划线
class Student():
    def __init__(self,name,place):
        self.name=name
        self.place=place
        print('my name is %s I am from %s' %(self.name,self.place))
    def talk(self):
        print('hello everybody!')
        
    def __hello(self):  #定义私有方法
        print('hello everybody')
        
stu1=Student('tom','Franch')   
stu1.talk()  
stu2=Student('poly','Italia')   
stu2.talk() 
#stu2.__hello()私有方法调用出错  


class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('my name is %s,I am %d years old.' %(self.name,self.age))
        
        
person1=Person('xiaoming',15)
person2=Person("dahua",18)        



