# -*- coding: utf-8 -*-
"""
Created on Mon May 28 22:47:52 2018

@author: Administrator
"""

import random
from time import sleep#调入包中的指定方法，用该import导入方法，方法前可以不加类名
from time import ctime
from class1 import Student

print(ctime())#查看当前时间
print(random.randint(0,100))#调用random方法产生随机数
sleep(3)
print('time over')

stu3=Student('lily','hujian')