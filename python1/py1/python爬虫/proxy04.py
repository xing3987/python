# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 23:03:36 2018

@author: Administrator
"""

'''
selenium代理
'''
from selenium import webdriver

proxy='127.0.0.1:8080'
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://'+proxy)
browser=webdriver.Chrome(chrome_options=chrome_options)
browser.get('http://httpbin.org/get')