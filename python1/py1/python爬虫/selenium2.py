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

#获取多个节点
lis=browser.find_elements_by_css_selector('.service-bd li')
'''
find_eliments_by_id
find_eliments_by_name
find_eliments_by_xpath
find_eliments_by_tag_name
find_eliments_by_css_selector
find_eliments(By.CSS_SELECTOR,'.service-bd li')
等
'''
print(lis)
browser.close()


'''
模拟点击输入文字等
'''
import time
browser=webdriver.Chrome()
browser.get('https://www.taobao.com')
input=browser.find_element_by_id('q')
input.send_keys('iphone')
time.sleep(5)
input.clear()
input.send_keys('ipad')
time.sleep(10)
button=browser.find_element_by_class_name('search-button')
print(button)
button.click()