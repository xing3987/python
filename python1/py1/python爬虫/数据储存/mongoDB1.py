# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 23:14:38 2018

@author: Administrator
"""

import pymongo

print(pymongo.version)
client=pymongo.MongoClient(host='localhost',port=27017)  #创建连接对象默认端口27017
#或client=MongoClient('mongodb://localhost:27017')
db=client.test  #指定数据库client['test']
collection=db.test #指定集合db['test']

student={'id':'003','name':'Jordan','age':20,'gender':'male'}
#插入数据
#result=collection.insert(student)  #insert方法已过时，用insert_one//insert_many替代
#print(result)

student1={'id':'002','name':'Marry','age':18,'gender':'female'}
#result=collection.insert_one(student1)
#print(result)
#print(result.inserted_id)

result=collection.insert_many([student,student1])  #插入多条数据
print(result.inserted_ids)

#查询(结果是条记录可以直接输出，多条记录结果是字典型遍历输出)
result=collection.find_one({'name':'Marry'})  #查询name为marry的对象，第一条数据
print(result)

results=collection.find() #select * from collection得到一个生成器，遍历取值
print(results)
for result in results:
    print(result)

from bson.objectid import ObjectId
result=collection.find_one({'_id':ObjectId('5b52f4ed3b70390fbc867123')})  #通过objectId查询每条数据都有一个hasy码,结果是字典型
print(result)

results=collection.find({'age':{'$gte':20}})
print('---------------age>=20:--------------')
for result in results:
    print(result)

'''
查询的比较符号
$lt   小于  {'age':{'$lt':20}}
$gt   大于
$lte   小于等于
$gte   大于等于
$ne    不等于
$in   在范围内   {'age':{'$in':[20,23]}}
$nin  不在范围内

$regex  匹配正则表达式  {'name':{'$regex':'^m.*'}}   #name以M开头
$exits  属性是否存在   {'name':{'$exits':True}}    #name属性存在
$type   类型判断       {'age':{'$type':'int'}}
$mod    数字模操作     {'age':{'$mod':[5,0]}}  #筛选年龄模5余0
$text  文本查询     {'$text':{'$search':'Mike'}}  #text类型的属性中包含Mike的字符串
$where   高级条件查询   {'$where':'obj.fans_count==obj.follow_count'}  #obj表示集合本身，自身粉丝数等于关注数
'''

results=collection.find({'$where':'obj.id<=obj.age'})
print('--------------where:id<age:--------------')
for result in results:
    print(result)
    
#计数count（）
count=collection.find().count()
print(count)

#排序sort()
results=collection.find().sort('name',pymongo.ASCENDING)  #以名字升序排列
print([result['name'] for result in results])

#偏移skip()
results=collection.find().sort('name',pymongo.ASCENDING).skip(10)  #忽略前十个数
print([result['name'] for result in results])

#指定获取的前几个结果limit()
results=collection.find().sort('name',pymongo.ASCENDING).limit(10)
print([result['name'] for result in results])

#skip()和limit()结合可做分页查询
print('-------分页-----')
results=collection.find().sort('name',pymongo.ASCENDING).skip(10).limit(10) 
print([result['name'] for result in results])
results=collection.find().sort('name',pymongo.ASCENDING).skip(20).limit(10)
print([result['name'] for result in results])
results=collection.find().sort('name',pymongo.ASCENDING).skip(30).limit(10)
print([result['name'] for result in results])

'''
#更新数据update()
condition={'name':'Jordan'}
student=collection.find_one(condition)
student['age']=2
result=collection.update(condition,{'$set':student})  #不使用$set则其他行都清空
#result=collection.update(condition,student)
print(result)
'''

print('-------更新数据最新方法update_one()和update_many()---------')

#更新数据update_one()
condition={'name':'Marry'}
student=collection.find_one(condition)
student['age']=2
result=collection.update_one(condition,{'$set':student})  #不使用$set则其他行都清空
#result=collection.update(condition,student)
print(result.matched_count,result.modified_count) #输出匹配的条数和影响的条数(数据改变的条数，如果值没有改变则不计入)

#更新年龄大于20第一条数据，使年龄加一
condition={'age':{'$gte':20}}
result=collection.update_one(condition,{'$inc':{'age':1}})  #年龄+1
print(result.matched_count,result.modified_count)

#update_many()更新年龄小于20所有数据，使年龄加一
condition={'age':{'$lt':20}}
result=collection.update_many(condition,{'$inc':{'age':1}})  #年龄+1
print(result.matched_count,result.modified_count)

print('-----------删除remove(),delete_one(),delete_many()---------------')
#remove()删除 
result=collection.remove({'age':{'$lte':3}}) #删除年龄小于等于3的数据
print(result)

#delete_one()删除一条符合条件数据
result=collection.delete_one({'name':'Marry'})
print(result,result.deleted_count)

#delete_many删除多条数据
result=collection.delete_many({'age':{'$gte':25}})
print(result,result.deleted_count)

'''
其他操作
find_one_and_delete()
find_one_and_replace()
find_one_and_update()
create_index()
create_indexes()
drop_index()等
'''





















































































