# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 22:11:13 2018

@author: Administrator
"""
#定义查询对象
people={
        'Alice':{'phone':'123','addr':'foo drive 23'},
        'Beth':{'phone':'323','addr':'Bar drive 44'},
        'Cecil':{'phone':'453','addr':'bza river 2'}
       } 

#定义查询项目
labels={
        'phone':'phone number',
        'addr':'address'
        }

#输入姓名，并输入查询什么
name=input('Name:')
request=input('search by Phone(p) or address(a)?')
if request=='p':
    key='phone'
else:
    key='addr'

#查询需要的结果
if name in people:
    print('%s`s %s is %s' %(name,labels[key],people[name][key])) #通过key得到值
    print('my phone number is %(phone)s' %people[name]) #可以把格式化的数据先写到%后面的（）中
else:
    print('input a wrong name!')