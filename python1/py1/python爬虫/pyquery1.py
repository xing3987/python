# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 21:34:20 2018

@author: Administrator
"""

'''
pyquery三种初始化方式
1.字符串
2.url
3.本地文件
'''

document=u'''
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

from pyquery import PyQuery as pq
doc=pq(document)
print(doc('li'))
print(doc('li a'))

#直接解析网址
doc=pq(url='https://cuiqingcai.com')
print(doc('title'))

#解析本地文件
#doc=pq(filename='demo.html')  文件无中文时可以直接这样使用
doc=pq(open('re目标文件.html','r',encoding='utf-8').read(),parser='html')  #有中文时必须这样读取
print(doc('a'))

#基本的css选择器
print('-----css选择器-----')
doc=pq(document)
print(doc('#list li:last'))
print(type(doc('#list li:last')))

               
#查找一个元素的特定子孙节点
lis=doc('#list')
item=lis.find('.active')  #只是子节点用children('.active')
print(item)               

item=lis.parent()  #查找父节点,parents()是父节点或祖父节点
print(item)

#获取兄弟节点
item=lis.siblings()
print(item)

print("------遍历------")
ass=doc('a').items()
for a in ass:
    print(a)
    print(a.attr('href'),a.attr.href) #获取属性
    print(a.text()) #获取文本
    print(a.html()) #获取标签内的内容，包括文本和子标签




























