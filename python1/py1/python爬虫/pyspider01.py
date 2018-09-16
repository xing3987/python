# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 00:24:18 2018

@author: Administrator
"""

from selenium import webdriver

browser=webdriver.PhantomJS()
browser.get('https://www.baidu.com')
print(browser.current_url)