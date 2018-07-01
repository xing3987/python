# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 23:56:36 2018

@author: Administrator

文本生成器
"""

def lines(file):
    for line in file:
        yield line
        yield '\n'

def blocks(file):
    block=[]
    for line in lines(file):
        if line.strip():
            block.append(line)            
        elif block:
            yield ''.join(block).strip()   #把开始和多余的空格删除
            block=[]
            