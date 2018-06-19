# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 16:48:59 2018

@author: Administrator
"""

'''
迭代器
'''

str1='hello world!'
iter1=iter(str1)

for x in iter1:
    print(x,end=' ')
 
iter2=iter(str1)
while True:
    try:
        x=next(iter2)  #可以用于获取对象
        if(x=='l'):
            print(x)
        else:
            print('a')
    except:
        break
        
print('\n'.join([' '.join('%d*%d=%2d' %(x,y,x*y) for x in range(1,y+1)) 
        for y in range(1,10)]))  #括号外面的在最外层，for y in range(1,10))
    
    
for y in range(1,10):
    for x in range(1,y+1):
        print('%d*%d=%2d\t' %(x,y,x*y),end='')  #注意加上end=''表示不会自动每行都打印
    print('') 
    
for y in range(1,10):
    for x in range(1,y+1):
        print('{}*{}={}\t'.format(x,y,x*y),end='')  #使用{}.format也可以
    print('') 