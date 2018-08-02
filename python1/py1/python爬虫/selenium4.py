# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 23:29:51 2018

@author: Administrator
"""

'''
使用selenium爬取淘宝商品(手机)数据，使用pyquery解析得到
商品图片，名称，价格，购买人数，店铺名称，并保存到MongoDB
'''

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from urllib.parse import quote
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser=webdriver.Chrome()
wait=WebDriverWait(browser,10)
key="手机"

#定义通过page得到商品的函数

def index_page(page):
    print('正在抓取第%s页' %page)
    try:
        url='https://s.taobao.com/search?q='+quote(key)
        browser.get(url)
        if page>1:
            input=wait.until(EC.presence_of_element_located((
                    By.CSS_SELECTOR,'#spulist-pager div.form>input.input.J_Input')))
            submit=wait.until(EC.element_to_be_clickable((
                    By.CSS_SELECTOR,'#spulist-pager div.form>span.btn.J_Submit')))
            input.clear()
            #print(input,submit)
            input.send_keys(page)
            submit.click()
        wait.until(EC.text_to_be_present_in_element((
                By.CSS_SELECTOR,'#spulist-pager li.item.active>span'),str(page)))
        wait.until(EC.presence_of_element_located((
                By.CSS_SELECTOR,'#main .grid-left')))
        print('加载完毕，开始分析页面')
    except TimeoutException:
        print("time out..page%s" %page)
        
index_page(3)