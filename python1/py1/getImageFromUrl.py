# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 23:29:11 2018

@author: Administrator
"""

import urllib
import urllib.request
import re

#定义页面加载的方法
def load_page(url):
    request=urllib.request.Request(url) #发起请求
    response=urllib.request.urlopen(request) #等待响应
    data=response.read() #获得响应数据
    return data #返回数据

#定义得到图片的方法,并放到本地磁盘
def get_image(html):
    regx='http://[\S]*jpg'      #确定正则表达式匹配图片url
    pattern=re.compile(regx)          #匹配正则表达式   
    get_image=re.findall(pattern,repr(html))  #获得匹配的数据集合,函数str() 用于将值转化为适于人阅读的形式，而repr() 转化为供解释器读取的形式
    num=1
    for img in get_image:
        image=load_page(img) #加载图片
        with open('D:/python/photo/%s.jpg' %num,'wb') as fb:  #创建一个目标文件(wb比特写入模式,注意文件夹一定要有)
            fb.write(image)  #写入图片byte数据
            print('正在下载第%s张图片' %num)
            num=num+1
            
    print('下载完成')
    
url='http://xiaohua.360.cn/jiongtu'    #创建目标连接'
html=load_page(url)     #加载目标的html对象
get_image(html)     #获得html对象中的jpg文件并保存












