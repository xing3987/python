# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 23:55:14 2018

@author: Administrator
"""
'''
自定义haskell
'''
class FunctionalList:
    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values
    
    def __len__(self):
        return len(self.values)
    
    def __getitem__(self, key):
        return self.values[key]
    
    def __setitem__(self, key, value):
        self.values[key] = value
    
    def __delitem__(self, key):
        del self.values[key]
    
    def __iter__(self):
        return iter(self.values)
    
    def __reversed__(self):
        return FunctionalList(reversed(self.values))
    
    def append(self, value):
        self.values.append(value)
    
    def head(self):
        # 获取第一个元素
        return self.values[0]
    
    def tail(self):
        # 获取第一个元素之后的所有元素
        return self.values[1:]
    
    def init(self):
        # 获取最后一个元素之前的所有元素
        return self.values[:-1]
    
    def last(self):
        # 获取最后一个元素
        return self.values[-1]
    
    def drop(self, n):
        # 获取所有元素，除了前N个
        return self.values[n:]
    
    def take(self, n):
        # 获取前N个元素
        return self.values[:n]