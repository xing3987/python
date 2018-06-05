# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 23:30:48 2018

@author: Administrator
"""

#执行多进程

import multiprocessing
from time import sleep,ctime

def talk(content,loop):
    for i in range(loop):
        print('start talk %s %s' %(content,ctime()))
        sleep(2)
    
def write(content,loop):
    for i in range(loop):
        print('start write %s %s' %(content,ctime()))
        sleep(2)
        
#定义进程并调用
process=[]
p1=multiprocessing.Process(target=talk,args=("hello world",2))
p2=multiprocessing.Process(target=write,args=('life is short,I am use python',2))
process.append(p1)
process.append(p2)

if __name__=='__main__':
    for p in process:
        p.start()
    for p in process:
        p.join()
    print('end..')