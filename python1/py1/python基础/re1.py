# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 23:48:29 2018

@author: Administrator
"""

'''
正则表达式
'''

import re

# 设定一个常量
a = 'asd34fiasodi341A1234DFYTH3241Yfjaosn3124dfans'

# 选择 a 里面的所有小写英文字母

re_findall = re.findall('[a-z A-Z]', a)

print(re_findall)

re_findnumber=re.findall('[\d]',a)

print(re_findnumber)

print(re.findall('A[\w]*Y',a))
#{}符号表示个数，*表示任意个
print(re.findall('d[\w]{3,9}a',a))

print(re.findall('[a-z]{3,9}',a))

'''
re.sub
实战过程中，我们很多时候需要替换字符串中的字符，这时候就可以用到 def sub(pattern, repl, string, count=0, flags=0)
函数了，re.sub 共有五个参数。其中三个必选参数：pattern, repl, string ; 两个可选参数：count, flags .

具体参数意义如下：

pattern	表示正则中的模式字符串(目标)
repl	repl，就是replacement，被替换的字符串的意思(替换后)
string	即表示要被处理，要被替换的那个 string 字符串
count	对于pattern中匹配到的结果，count可以控制对前几个group进行替换（替换几个）
flags	正则表达式修饰符
具体使用可以看下下面的这个实例，注释都写的很清楚的了，主要是注意一下，第二个参数是可以传递一个函数的，
这也是这个方法的强大之处，例如例子里面的函数 convert ,对传递进来要替换的字符进行判断，替换成不同的字符。
'''

sub1=re.sub('s','***',a,1)
print(sub1)

#被替换的字符可以是一个函数，用来条件替换，对前面正则匹配多个数的补充

#把s替换成***，A替换成---
def convert(value):
    group=value.group()
    if(group=='s'):
        return '***'
    elif(group=='A'):
        return '---'
    
sub2=re.sub('[sA]',convert,a)
print(sub2)

sub3=re.sub('s[\w]*a','*xx',a)  
print(sub3)
    
    




















