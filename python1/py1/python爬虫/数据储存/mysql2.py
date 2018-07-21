# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 23:34:14 2018

@author: Administrator
"""

#标准化插入语句（可以写成方法，传入db,table,data）
import pymysql

db=pymysql.connect(host='localhost',user='root',password='root',port=3306,db='spiders')
cursor=db.cursor()

data={'id':'006','name':'tom','age':20}  #数据传入改为字典
table='students'
keys=','.join(data.keys())
values=','.join(len(data.values())*['%s'])
sql='insert into {table}({keys}) values({values})'.format(table=table,keys=keys,values=values)
print(sql,tuple(data.values()))
try:
    if cursor.execute(sql,tuple(data.values())):
        print('successful')
        db.commit()
except:
    print('Failed')
    db.rollback()

db.close()


#标准化更新数据（可以写成方法，传入db,table,data)
'''
普通执行语句:
sql='update students set age=%s where name=%s'
try:
    if cursor.execute(sql,(25,'Bob')):
        print('successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
'''

#如果主键不存在则插入数据，主键存在则更新数据
db=pymysql.connect(host='localhost',user='root',password='root',port=3306,db='spiders')
cursor=db.cursor()
data={'id':'006','name':'Bob','age':25}

table='students'
keys=','.join(data.keys())
values=','.join(len(data)*['%s'])
#on duplicate key当主键相同时执行update...
sql='insert into {table}({keys}) values({values}) on duplicate key update '.format(table=table,keys=keys,values=values)
update=','.join(["{key}=%s".format(key=key) for key in data])  #把生成的数字用“，”连接转成字符串
sql+=update
print(sql)
try:
    if cursor.execute(sql,tuple(data.values())*2):
        print('successful')
        db.commit()
except:
    print('failed')
    db.rollback()
db.close()


print(["{key}=%s".format(key=key) for key in data]) #生成一个数组





























