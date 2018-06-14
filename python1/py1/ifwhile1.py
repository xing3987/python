# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 23:24:08 2018

@author: Administrator
"""
#遍历字典
d={'x':4,'y':2,'z':3}
for key in d:
    print(d.get(key),'or',d[key])
    
#使用并行迭代
names=['anne','beth','george','damon'] 
ages=[12,32,33,21]

for i in range(len(names)):
    print(names[i],'is age:',ages[i])
    