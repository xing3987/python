# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 23:28:25 2018

@author: Administrator
"""

'''
进程和守护进程
'''

import multiprocessing
import time


def worker(x):
    print('工作开始时间：%s' %time.ctime())
    time.sleep(x)
    print('工作结果时间：%s' %time.ctime())

p = multiprocessing.Process(target=worker,args=(2,))
if __name__ == '__main__': 
    p.start()
    p.daemon=True
    print('【EMD】')