# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 22:50:07 2018

@author: Administrator
"""

#闭包的使用

time=0
def insert_time(min):
    global time  #使用globel关键子,可以调用全局变量，并改变值后返回
    time+=min    #全局变量作为局部变量使用，并且改变了值，没有globel会报错
    return time

print(insert_time(2))
print(time)
print('#############')

'''
使用闭包，在不改变全局属性time的情况下使用全局变量
所有函数都有一个 __closure__ 属性，如果函数是闭包的话，那么它返回的是一个
由 cell 组成的元组对象。cell 对象的 cell_contents 属性就是存储在闭包中的变量
'''

times=0
def study_time(times):
    def insert_times(min):
        nonlocal times #nonlocal 关键字,表示在函数或其他作用域中使用外层(非全局)变量
        times+=min
        return times
    return insert_times

f=study_time(times)
print(f.__closure__)
print(f(2))
print(f.__closure__[0].cell_contents)  #获取闭包中的值
print(times)
print(f(10))
print(times)
print(f.__closure__[0].cell_contents)
