# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 21:56:15 2018

@author: Administrator
"""

#保存知乎上‘发现’页面的‘热门话题’，将器问题和答案统一保存成文本形式

import requests
from pyquery import PyQuery as pq

url="https://www.zhihu.com/explore" 

headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'        
        }

html=requests.get(url,headers=headers).text
doc=pq(html)

items=doc('.explore-tab .explore-feed').items()
for item in items:
    question=item.find('h2').text()
    #print(question)
    author=item.find('.author-link').text()
    #print(author)
    answer=pq(item.find('.content').html()).text()  #.replace(' ','').strip()  #找出回复中的文本并去掉空格
    #print(answer)
    with open('zhihu_explore.txt','a',encoding='utf-8') as file:  #创建要写入的文件，注意格式,这种方式打开相对于直接open可以不写close()
        file.write('\n'.join([question,author,answer]))
        file.write('\n'+'='*50+'\n') #增加段落的分隔
        #file.close()

