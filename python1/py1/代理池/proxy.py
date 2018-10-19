# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 22:37:59 2018

@author: Administrator
"""

tester_cycle=20
getter_cycle=20
tester_enabled=True
getter_enabled=True
api_enabled=True
api_host='localhost'  
api_port=7070   

from proxypool04 import app
from proxypool03 import Getter,Tester
import time
import threading

class Scheduler():
    def schedule_tester(self,cycle=tester_cycle):
        tester=Tester()
        while True:
            print('begin test:')
            tester.run()
            time.sleep(cycle)
            
    def schedule_getter(self,cycle=getter_cycle):
        getter=Getter()
        while True:
            print('begin crawl:')
            getter.run()
            time.sleep(cycle)
                
    def schedule_api(self):
        app.run(api_host,api_port)

    def run(self):
        print('begin crawl proxypool:')
        threads=[]
        if tester_enabled:
            #tester_process=Process(target=self.schedule_tester)
            tester_thread=threading.Thread(target=self.schedule_tester)
            #tester_process.start()
            threads.append(tester_thread)
            
        if getter_enabled:
            #getter_process=Process(target=self.schedule_getter)
            getter_thread=threading.Thread(target=self.schedule_getter)
            #getter_process.start()
            threads.append(getter_thread)
            
        if api_enabled:
            #api_process=Process(target=self.schedule_api)
            api_thread=threading.Thread(target=self.schedule_api)
            #api_process.start()
            threads.append(api_thread)
        
        for t in threads:
            t.start()
        for t in threads:   
            t.join()
         
scheduler=Scheduler()
scheduler.run()











