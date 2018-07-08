# -*- coding: utf-8 -*-
"""
Created on Mon May 28 23:55:40 2018

@author: Administrator
"""

'''
python异常处理try......except.......
   FileNotFoundError 文件不存在异常
   NameError 文件名错误异常
   BaseException 基本通用异常
'''
try:
    fileName=input('please input fileName:')
    open('%s.py' %fileName)
except FileNotFoundError:
    print('the file %s.py your input is wrong' %fileName)

#打印系统自带的异常提示信息
try:
    print(stu)
except BaseException as msg:
    print(msg)
else:#后面可以接else，表示不发生异常输出
    print('ok')
    
#finally无论是否异常都打印
try:
    print('finally:')
except BaseException:
    print("Exception")
finally:
    print('Exception over')
    
#raise抛出异常
def throwException(x,y):
    if y==0:
        raise BaseException('y can not be zero')
    return x/y

try:
    throwException(10,0)
except BaseException as msg:
    print(msg)
    
    
    
    