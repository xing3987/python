# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 22:54:17 2018

@author: Administrator
"""

import pymysql

#创建数据库
db=pymysql.connect(host='localhost',user='root',password='root',port=3306) 
cursor=db.cursor()  #获得执行对象
cursor.execute('select version()')
data=cursor.fetchone()  #得到最后一次执行的第一条数据
#cursor.execute('show databases')  
data=cursor.fetchone()
print('Database:',data)
#cursor.execute('create database spiders default character set utf8')
db.close()


#创建talbe
db=pymysql.connect(host='localhost',user='root',password='root',port=3306,db='spiders') #最后的参数指定数据库
cursor=db.cursor()
sql='create table if not exists students(id varchar(255) not null primary key,name varchar(255) not null,age int not null)'
#cursor.execute(sql)
db.close()

#插入数据(需要db.commit而且是事物，注意异常回滚)
id='007'
user='Bob'
age=20

db=pymysql.connect(host='localhost',user='root',password='root',port=3306,db='spiders')
cursor=db.cursor()
sql=('insert into students values("%s","%s",%s)' %(id,user,age))
print(sql)
try:
    cursor.execute(sql)  #两种执行方法，一种直接执行sql
    #sql='insert into students values("%s","%s",%s)'
    #cursor.execute(sql,(id,user,age)) #一种执行sql，传入turple参数
    db.commit()
    print('success.')
except BaseException as msg:
    print('插入失败：',msg)
    db.rollback()
db.close()
