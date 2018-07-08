# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 22:11:14 2018

@author: Administrator
"""

from copy import deepcopy

d={}
d['names']=['lily','lucy']
print(d)
c=d.copy() #普通复制，当原来的字典元素改变时，复制后的字典也一起改变
print(c)
dc=deepcopy(d) #深度复制，当原来的字典元素改变时，复制后的字典不受影响
print(dc)
d['names'].append('xiaoming')
print(d)
print(c)
print(dc)

print(d.get('what'))  #通过key查询值，与d['name']的区别是可以得到null值
print(d.get('names','hello')) #get第二个参数为默认值，当key不存在时，显示第二个参数的值
