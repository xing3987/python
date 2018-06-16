# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 23:24:08 2018

@author: Administrator
"""
#遍历字典
d={'x':4,'y':2,'z':3}
for key in d:
    print(key,':',d.get(key),'or',d[key])

for key,value in d.items():  #d.items()把数组转成元组返回，然后就可以直接迭代输出键值
    print(key,value)
    
#使用并行迭代
names=['anne','beth','george','damon'] 
ages=[12,32,33,21]

for i in range(len(names)):
    print(names[i],'is age:',ages[i])
'''   
zip函数可以把两个序列压缩在一起，返回一个元组的列表,可以用来压缩不等长序列，短的用完就结束  
'''   
zip(names,ages)  

for name,age in zip(names,ages):
    print(name,age)
    
#找出名字中含a的人，并把他们的名字换成tom    
index=0
for name in names:
    if 'a' in name:
        names[index]='tom'
    index+=1
print(names)

print(sorted(ages))  #sort排序

'''
for 循环可以用else来表示不在循环中的情况（一般循环中要带break跳出循环，要不然else总会在最后执行）
'''
from math import sqrt
for num in range(99,0,-1):
    if sqrt(num)==int(sqrt(num)):
        print('找到了可以开根号的数为%d' %num)
        #break
else:
    print('没有找到~~')
    
    
#列表推导式(生成特定序列)
nums=[x*x for x in range(10)]
print(nums)

nums1=[x*x for x in range(10) if x%3==0]
print(nums1)


x=20
if x<0:
    print('负数')
elif  0<x<100:
    #还没写
    pass   #如果没写东西程序会报错必须用pass跳过
else:
    print('大于100')











    