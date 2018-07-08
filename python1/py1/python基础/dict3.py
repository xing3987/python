# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 22:45:02 2018

@author: Administrator
"""

if 1!=2: print ('gogogo')
print(2**3)  #乘方
print(pow(2,3)) #乘方

print(abs(-10)) #绝对值
print(round(3.5)) #四舍五入

import math
print(math.floor(3.5)) #向下取整
print(math.floor(-3.5))

print("Let\'s go")  #可以用\转义，也可以合理使用"'
print(r"http:\\nihao\\gogo")  #r加上字符串表示原始字符串，可以不用转义，直接打印本身
print("http:\\go\\")
print("python"*5)
'''
列表和元组
'''
number=[0,1,2,3,4,5,6,7,8,9]
print(number[0:5]) #输出第0到5位数，含头不含为
print(number[0:5:2]) #步长为2，即隔一位输出
print(number[10:5:-1]) #步长为负数时，从左边取元素

#例：在盒子中打印一个句子
 
message=input("please input your message:")
textWidth=len(message)
screenWidth=textWidth+40
boxWidth=textWidth+8
margin=int((screenWidth-boxWidth)/2)

print (' '*margin+'+'+'-'*boxWidth+'+')
print(' '*(margin+3)+'|'+' '*(textWidth+2)+'|')
print(' '*(margin+3)+'|'+' '+message+' |')
print(' '*(margin+3)+'|'+' '*(textWidth+2)+'|')
print (' '*margin+'+'+'-'*boxWidth+'+')

#####################################

print(1 in number) #判断列表中是否包含一个元素使用in
print(number.index(5)) #查询元素的位置

'''
元组就是不可变的序列
'''
numberX=tuple(number)  #tuple是把序列转化成元组
print(numberX)
print(number)









