# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 15:50:50 2018

@author: Administrator
"""
'''
超类和继承
'''

class Calculator:
    def calculate(self,value):
        self.value=value

class Talker:
    def talk(self):
        print('Hi,my vlaue is %s' %self.value)
        
class Talking(Calculator,Talker):
    pass


a=Talking()
a.calculate(12)
a.talk()


class Bird:
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry:
            print('Aaaah...')
            self.hungry=False
        else:
            print('No,thanks!')

class SongBird(Bird):
    def __init__(self):
        super(SongBird,self).__init__()  #调用父类的初始化方法也可以用：Bird.__init__(self)
        self.sound='hello~'
    def sing(self):
        print(self.sound)
    @classmethod       #类的方法，使用固有类名.方法名访问   
    def speak(self):
        print('I am Poly')
    @property        #是方法变成属性一样被调用,没有括号
    def hi(self):
        print('hi!')
                     

sb=SongBird()
sb.sing()
sb.eat()
sb.eat()
SongBird.speak()
sb.hi

print(isinstance(sb,Bird))  #判断一个实例是否属于一个父类，第二个参数要是父类名
print(isinstance('aa',str))  
























