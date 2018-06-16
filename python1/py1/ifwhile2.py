# -*- coding: utf-8 -*-
"""
Created on Wed May  2 20:35:31 2018

@author: Administrator
"""

#条件判断
score=85
if score>80:
    print('优秀')
elif score>=60:
    print('合格')
else:
    print('重修')
    
student=[1,2,3,4]
for stu in student:
    print(stu)
else:
    print('结束')
    
#range()生成一个整数序列
sum=0
for i in range(11):
    sum=sum+i
print(sum)

#猜数字小游戏
import random
n=int(input('请猜数字：'))
num1=random.randint(1,100)
t=0
while n!=num1:
    if n>num1:
        print('大了')
      #  n=int(input('请猜数字：'))
    elif n<num1:
        print('小了')
    t=t+1
    if t==8:
        print('你输了，没猜出来')
        break
    n=int(input('请猜数字：'))
else:
     print('你赢了，猜对了')