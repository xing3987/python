# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 00:20:16 2018

@author: Administrator
"""

from selenium import webdriver

browser=webdriver.PhantomJS()
browser.get('https://www.baidu.com')
print(browser.current_url)
print(browser.page_source)