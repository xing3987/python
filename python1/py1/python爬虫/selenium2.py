# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 23:50:03 2018

@author: Administrator
"""

#多种选择器
from selenium import webdriver
from selenium.webdriver.common.by import By

browser=webdriver.Chrome()
browser.get('https://www.taobao.com')
input1=browser.find_element_by_id('q')  #id选择器
input2=browser.find_element_by_css_selector('#q')  #css选择器
input3=browser.find_element_by_xpath('//input[@id="q"]')  #xpath选择器
input4=browser.find_element(By.ID,'q') #同input1
print(input1,input2,input3,input4)
browser.close()
                                            