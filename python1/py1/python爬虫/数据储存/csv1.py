# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 23:36:18 2018

@author: Administrator
"""

import csv

with open('csvdata.csv','w') as file:
    writer=csv.writer(file)  #默认逗号为分隔符 
    writer.writerow(['id','name','age'])
    writer.writerow(['1','tom','10'])
    writer=csv.writer(file,delimiter=' ') #改变分隔符为空格
    writer.writerow(['2','jams','15'])
    writer.writerows([['3','poli','16'],['4','guge','26']]) #同时写入多行注意最外层要用[]包围

#写入字典型的数据
with open('csvdata.csv','a',encoding='utf-8') as file:  #如果有中文注意编码
    fieldnames=['id','name','age']
    writer=csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader() #写出头部filenames
    writer.writerow({'id':'1001','name':'小王','age':'20'})
    writer.writerow({'id':'1002','name':'大牛','age':'28'})
    
#读取csv文件
with open('csvdata.csv','r',encoding='utf-8') as file:  #如果有中文注意编码
    reader=csv.reader(file)
    for row in reader: #遍历行读取
        print(row)
        
#使用pandas读取,显示更友好
import pandas as pd

df=pd.read_csv('csvdata.csv')
print(df)