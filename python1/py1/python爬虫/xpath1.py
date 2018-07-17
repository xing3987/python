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
document=u'''
<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class=introduction">经典老歌列表</p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
    </ul>
</div>
'''
#print(document)

from lxml import etree

f1=open('re目标文件.html','rb')  #因为文件有汉字所以要用rb读取
context=f1.read().decode('utf-8')
html=etree.HTML(context)  #可以使用该函数读取r.text字符串

'''
html=etree.HTML(context,parser=etree.HTMLParser(encoding='utf-8'))  #读取str字符解析
result=etree.tostring(html)
print(result.decode('utf-8'))

#直接读取文件解析
html=etree.parse('re目标文件.html',etree.HTMLParser())  #直接读取文件解析
result=etree.tostring(html)
print(result.decode('utf-8'))
'''
#使用xpath函数
#html=etree.parse('re目标文件.html',etree.HTMLParser())  #直接读取文件解析
result=html.xpath('//*')  #得到所有子节点和集合
print(result)
print(result[0])

#得到a标签的节点

result=html.xpath('//li/a')  #得到所有li中的a子节点和集合
print(result)
print(result[0])

result1=html.xpath('//ul//a')  #得到所有ul中的a子孙节点和集合
print(result1)

#获取属性
print('-------属性------')
result=html.xpath('//a/@singer')
print(result[0])

#通过子节点得到父节点..
#获取<a href="/3.mp3" singer="齐秦">往事随风</a>父节点的class属性：
result=html.xpath('//a[@href="/3.mp3"]/../@class')  #或使用parent::*代替..
print(result)

html=etree.HTML(context,parser=etree.HTMLParser(encoding='utf-8'))  #读取str字符解析
result=etree.tostring(html)


























