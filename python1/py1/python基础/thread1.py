# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 22:50:20 2018

@author: Administrator

进程和多线程的应用
"""

from time import ctime,sleep
import threading #导入线程的架包
import multiprocessing

def talk():
    print('start talk %r' %ctime())
    sleep(2)
    
def write():
    print('start write %r' %ctime())
    sleep(3)
'''
#########    定义main方法      ###########    
if __name__=='__main__':
    for i in range(3):
        talk()
        write()
'''        
#线程的应用
def talk(content,loop):
    for i in range(loop):
        print('start talk %s %s' %(content,ctime()))
        sleep(2)
    
def write(content,loop):
    for i in range(loop):
        print('start write %s %s' %(content,ctime()))
        sleep(2)
  
threads=[]
t1=threading.Thread(target=talk,args=('helloWorld',2))
t2=threading.Thread(target=write,args=('life is short,your need python',3))
threads.append(t1)
threads.append(t2)

#执行多线程
if __name__=='__main__':
    for t in threads:
        t.start()
    for t in threads: #遍历线程，使线程同步执行！  
        t.join()
    print('all thread end!')

'''
#定义进程并调用
processes=[]
p1=multiprocessing.Process(target=talk,args=("hello world",2))
p2=multiprocessing.Process(target=write,args=('life is short,I am use python',2))
processes.append(p1)
processes.append(p2)

if __name__=='__main__':
    for p in processes:
        print('process')
        p.start()
    for p in processes:
        p.join()
    print('end..')

'''    












     
