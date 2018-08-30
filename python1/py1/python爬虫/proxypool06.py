# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 00:56:14 2018

@author: Administrator
"""

import requests

proxy_pool_url="http://127.0.0.1:7070/random"

def get_proxy_pool():
    try:
        response=requests.get(proxy_pool_url)
        if response.status_code==200:
            return response.text
    except ConnectionError:
        return None
    
print('获得一个代理池中的代理：'+get_proxy_pool())