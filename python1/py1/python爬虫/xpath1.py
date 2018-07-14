# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 20:17:34 2018

@author: Administrator
"""

'''
XPath常用规则

nodename 选取此节点的所有子节点
/ 从当前节点选取直接子节点
// 从当前节点选取子孙节点
.  选取当前节点
..  选取当前节点的父节点
@  选取属性


例：
    //title[@lang='eng']   选择所有名称为title,同时属性lang值为eng的节点
'''
from lxml import etree

f1=open('re目标文件.html','rb')  #因为文件有汉字所以要用rb读取
context=f1.read().decode('utf-8')

html=etree.HTML(context)  #读取str字符解析
result=etree.tostring(html)
print(result.deocode('utf-8'))

html=etree.parse('re目标文件.html',etree.HTMLParser())  #直接读取文件解析
result=etree.tostring(html)
print(result.deocode('utf-8'))


