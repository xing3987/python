# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 18:09:21 2018

@author: Administrator
"""

#import this
#转义字符
print('hello world')
print('hello \'world','\n\t你好')
print('c:\\python35\\myPython')

print('are','you','ok')
width=30
print('width is %d' %width)
str='你好'
print('say %s' %str)

"""
输入框
con=input('请输入：')
print('他说 %r' %con)
"""

#数据加减
x=5
y=1.3
print(x+y)

#boolean类型(大写开头)
b1=True
b2=False
print(b1 and b2)

#数组
student=['jack','bob','harry','micle']
print(student)
print(student[0])
print(student[-1])
student.append('toli')#添加
print(student)
student.pop()#末尾删除元素
student.pop(2)#删除指定位置元素
print(student)

#元组：与列表类似，但是定义后不能修改使用小括号
teacher=('marry','pitter','python')
print(teacher[0])
print(teacher[0:2])#含前不含后
print(teacher[1:])#从第几个开始
print(teacher[:1])#从第几个结束
print(len(teacher))#求数组长度
print(max(teacher))#求数组最大值

#字典：是一种可变容器模型，且可存储任意类型对象，键值对储存，类似map
#使用大括号定义
body={1:'jack',2:'bobo',3:'marry',4:'micle'}
print(body[3])#访问指定键的值
body[5]='kemmy'#添加或者更改
del body[1]#删除指定key
print(body)
body.clear()#清空
print(body)
del body#删除整个字典














