# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 22:49:31 2018

@author: Administrator
"""

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

from scrapy import Selector

selector=Selector(text=document)

print(selector.xpath('//li/a/text()').extract_first())  #Selector调用xpath选择器，extract_first()得到结果集中的第一个，该方法还可以设置取不到值时默认返回值如：extract_first('default')

print(selector.xpath('//li').xpath('./a/text()').extract_first())  #使用‘./’表示从当前元素开始提取，使用'//'则从最外层开始提取

print(selector.xpath('//li').xpath('./a/@singer').re('[a-z]+'))  #可以直接使用re正则匹配，筛选结果含a-z字母的歌手re_first()方法可直接获取第一个值
