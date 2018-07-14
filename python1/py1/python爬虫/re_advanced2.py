# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 00:02:24 2018

@author: Administrator
"""
import re

f1=open('re目标文件.html','rb')  #因为文件有汉字所以要用rb读取
context=f1.read().decode('utf-8')

#匹配class='active'中的歌手和歌名
result=re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>',context,re.S)
print(result.group(1),result.group(2))


#匹配文章中第一个歌手和歌名
result=re.search('<li.*?singer="(.*?)">(.*?)</a>',context,re.S)
print(result.group(1),result.group(2))

#如果去掉re.S则会匹配到不换行的<li>中的第一个歌手和歌名
result=re.search('<li.*?singer="(.*?)">(.*?)</a>',context)
print(result.group(1),result.group(2))



f1.close()


#findal()函数是查找所有符合条件的数据，结果是一个元组类型的列表
results=re.findall('<li.*?singer="(.*?)">(.*?)</a>',context,re.S)
print(results)
print(results[0][0])
for result in results:
    print(result[0],result[1])  #元组没有group()只能用下标表示
    
#compile()可以将正则字符串编译成正则表达式对象，用于重复使用,里面可以加上re.S等修饰符，它是对正则的一种封装
#sub()用于替换正在匹配到的数据：第一个参数为正则表达式，第二个为替换后的数据，第三个为目标字符
content1='2016-11-15 12:00'
content2='2015-12-11 11:11'
content3='2017-2-21 1:20'
pattern=re.compile('\d{1,2}:\d{2}') #匹配时间
time1=re.sub(pattern,'',content1)  #时间替换成空
time2=re.sub(pattern,'',content2)
time3=re.sub(pattern,'',content3)
print(time1,time2,time3)

