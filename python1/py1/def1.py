# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 20:29:05 2018

@author: Administrator
"""

#递归

def power(x,n):
    if n==0:
        return 1
    else:
        return x*power(x,n-1)
    
print(power(2,3))
def search(sequence,number,lower=0,upper=None):
    if upper is None:upper=len(sequence)-1
    if lower==upper:
        assert number==sequence[upper]
        return upper
    else:
        middle=(lower+upper)//2
        if number>sequence[middle]:
            return search(sequence,number,middle+1,upper)
        else:
            return search(sequence,number,lower,middle)

seq=[34,67,8,123,4,100,95]
#seq.sort()  #sort方法是无返回对象的，该方法把原来的序列进行排序
#print(seq) 
seq1=sorted(seq)  #sorted方法传入一个序列为参数，返回一个排序后的序列
print(seq1)
print(search(seq1,8))