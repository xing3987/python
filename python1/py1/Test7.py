# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 21:23:00 2018

@author: Administrator

读取xml文件
    nodeName:节点名
    nodeType:节点类型(元素节点返回1，属性节点返回2)
    nodeValue:节点值（没有文本对象，返回none）
"""

from xml.dom import minidom  #导入xml的读取架包

dom=minidom.parse("class.xml")
root=dom.documentElement  #读取根元素
print(root.nodeName)
print(root.nodeType)
print(root.nodeValue)
print('*******************')
ids=dom.getElementsByTagName('id')
names=dom.getElementsByTagName('name')
ages=dom.getElementsByTagName('age')
for i in range(3):
    print(ids[i].firstChild.data) #注意要加firstChild
    print(ids[i].firstChild.nodeValue)
    print(names[i].firstChild.data)
    print(ages[i].firstChild.data)
    
#获取属性值
some=dom.getElementsByTagName('some')
print(some[0].getAttribute('ip'))