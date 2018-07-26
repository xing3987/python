# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 22:53:22 2018

@author: Administrator
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser=webdriver.Chrome()  #打开一个谷歌客户端
'''
browser=webdriver.Chrome()  谷歌
browser=webdriver.Firefox()  火狐
browser=webdriver.Edge()    Edge
browser=webdriver.PhantomJS()   PhantomJS无界面浏览器
browser=webdriver.Safari()   苹果
'''

try:   
    browser.get('https://www.baidu.com') #输入网址
    input=browser.find_element_by_id('kw') #获取搜索框
    input.send_keys('Python')  #发送搜索内容
    input.send_keys(Keys.ENTER) #发送确定
    wait=WebDriverWait(browser,10)
    wait.until(EC.presence_of_element_located((By.ID,'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
    #print(browser.page_source)  #得到页面内容
finally:
    browser.close()
