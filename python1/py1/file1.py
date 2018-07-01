# -*- coding: utf-8 -*-
"""
Created on Wed May 30 22:55:48 2018

@author: Administrator
"""

'''
文件管理
open(filename,model,buffering)
filename:文件路径，注意\要转义成\\
modle：读取模式：r(只读),w(覆盖写入),rb(二进制形式打开只读),a(用于追加写入)
'''

f1=open('11.txt','r')
f2=open('D:\\python\\python1\py1\\11.txt','r')
line1=f1.read()
line2=f2.readline()
line3=f2.readlines()#得到f2的以行算的数祖
print('line1:',line1)
print('line2:',line2)
print('line3:',line3)

for line in line3:
    print(line.split(",")[0])#如果一行有多个数可以分隔打印
    
'''
文件的写入
f3=open('11.txt','w')
f3.write('helloworld')
'''    

'''
csv文件的读取写入
'''
import csv

#读取
csvFile=csv.reader(open('12.csv','r'))
for stu in csvFile:
    print(stu)

#写出，先打开文件，再把数据写入
tofile=open('12.csv','a')
stu1=['a','aa','aaa']
stu2=['b','bb','bbb']
csvWriter=csv.writer(tofile,dialect='excel')#设定写入模式，默认excel
csvWriter.writerow(stu1)#写入具体内容
csvWriter.writerow(stu2)
tofile.close()






















