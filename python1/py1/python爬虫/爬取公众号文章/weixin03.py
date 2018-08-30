# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 22:33:33 2018

@author: Administrator
"""

'''
使用mysql保存抓取到的数据,先在spiders(database)中建表artiles
'''

mysql_host="127.0.0.1"
mysql_user='root'
mysql_password='root'
mysql_port=3306;
mysql_database='spiders'


import pymysql

class MysqlWx():
    def __init__(self,host=mysql_host,username=mysql_user,password=mysql_password,port=mysql_port,database=mysql_database):
        try:
            self.db=pymysql.connect(host,username,password,database,charset='utf8',port=port)
            self.cursor=self.db.cursor()
        except pymysql.MySQLError as e:
            print(e.args)
            
    def insert(self,table,data):
        keys=','.join(data.keys())
        values=','.join(['%s']*len(data))
        sql='insert into {table}({keys}) values({values})'.format(table=table,keys=keys,values=values)
        try:
            self.cursor.execute(sql,tuple(data.values()))
            self.db.commit()
        except pymysql.MySQLError as e:
            print(e.args)
            self.db.rollback()
    
    def selectAll(self,table):
        sql='select * from {table}'.format(table=table)
        try:
            self.cursor.execute(sql)
            results=self.cursor.fetchall()
            print(results)
        except pymysql.MySQLError as e:
            print(e.args)
            
#MysqlWx().selectAll('articles')