# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 22:33:44 2018

@author: Administrator
"""

import pymysql

db=pymysql.connect(host='localhost',user='root',password='root',port=3306,db='spiders')
cursor=db.cursor()

#删除数据
table='students'
condition='age>20'
sql='delete from {table} where {condition}'.format(table=table,condition=condition)
print(sql)
try:
    if cursor.execute(sql):
        db.commit()
        print('delete successed')
except:
    print('delete failed')
    db.rollback()


#查询数据
sql='select * from students where age<=20'
try:
    cursor.execute(sql)
    print('count:',cursor.rowcount)  #得到结果行数
    one=cursor.fetchone() #得到第一行数据
    print('one:',one)
    results=cursor.fetchall() #得到所有剩下的数据，当前面没有fetchone时得到所有数据
    print(results) #类型是元组类
    print('type:',type(results))
    for row in results: #遍历得到每组数据
        print(row)
except:
    print('Error')
print('--------循环按行取数据-------------')    
#一行行的取得数据   
try:
    cursor.execute(sql)
    print('count:',cursor.rowcount)  #得到结果行数
    row=cursor.fetchone() #得到第一行数据
    while row:
        print('row:',row)
        row=cursor.fetchone()
except:
    print('Error')
    
    

db.close()