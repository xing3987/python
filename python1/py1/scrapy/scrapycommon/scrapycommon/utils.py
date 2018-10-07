# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 23:20:12 2018

@author: Administrator
"""

from os.path import realpath,dirname
import json

def get_config(name):
    path=dirname(realpath(__file__))+'/configs/'+name+'.json'  #dirname(realpath(_file__))可以得到当前文件夹的路径
    with open(path,'r',encoding='utf-8') as f:
        return json.loads(f.read())
    
def china(start,end):
    for page in range(start,end+1):
        yield 'https://tech.china.com/articles/index_'+str(page)+'.html'
    