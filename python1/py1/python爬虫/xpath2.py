# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 12:43:48 2018

@author: Administrator
"""

document='''
<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class=introduction">经典老歌列表</p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐" name="one">沧海一声笑</a>
        </li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐" name="two">沧海一声笑</a>
        </li>
        <li data-view="4" class="active right">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
    </ul>
</div>
'''
#print(document)

from lxml import etree

html=etree.HTML(document)
result=html.xpath('//a/@singer')
print(result[0])

#获取节点中的文本
result=html.xpath('//a/text()')  #li标签的文本是‘\n  ’换行符
print(result)

#多个属性值时的定位，contains:获取class含right的a标签文本
result=html.xpath('//li[contains(@class,"right")]/a/text()')
print(result)

#使用and匹配多个条件
result=html.xpath('//a[@href="/2.mp3" and @name="two"]/text()')
print(result)

#按顺序选取节点
print('-------顺序取节点-------')
result=html.xpath('//li[2]/a/text()')  #选取第二个li标签的a节点文本（这里下标从1开始）
print(result)

result=html.xpath('//li[last()]/a/text()') #选取最后一个li标签的文本
print(result)

result=html.xpath('//li[position()<4]/a/text()') #选取为值小于4（1,2,3）的li文本
print(result)

result=html.xpath('//li[last()-1]/a/text()') #选取倒数第二个的li文本
print(result)



























