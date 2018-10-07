# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 23:28:06 2018

@author: Administrator
"""

from os.path import realpath,dirname
#import json

def get_config(name):
    path=dirname(realpath(__file__))+'/'+name+'.py'  #dirname(realpath(_file__))可以得到当前项目的路径
    print(path)
    with open(path,'r',encoding='utf-8') as f:
#        return json.loads(f.read())
        print(f.read())
 
    
get_config('getpath01')