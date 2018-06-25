# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 22:49:40 2018

@author: Administrator
"""

#线程的创建

import time
import threading

class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            print('thread {},@number:{}'.format(self.name,i))
            time.sleep(2)
            
def main():
    print('Start main threading')
    
    #创建三个线程
    threads=[MyThread() for i in range(3)]
    #启动三个线程
    for t in threads:
        t.start()
    #使用Join是子线程运行完了再运行主线程
    for t in threads:
        t.join()
    
    print('end main threading')
    
if __name__=='__main__':
    main()
    

