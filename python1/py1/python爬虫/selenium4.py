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

'''
#chrome Headless模式(无界面模式)
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser=webdriver.Chrome(chrome_options=chrome_options)
'''

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
        
        wait.until(EC.presence_of_element_located((
                By.CSS_SELECTOR,'.grid-item .grid-panel'))) #等待直到css选择的东西加载完毕
        wait.until(EC.text_to_be_present_in_element((
                By.CSS_SELECTOR,'#spulist-pager .item.active>span'),str(page)))        
        get_product1()
    except TimeoutException:
        print("time out..page%s" %page)
        
#定义爬取商品数据的函数
from pyquery import PyQuery as pq
def get_product1():
    print('加载完毕，开始分析页面')
    html=browser.page_source
    doc=pq(html)
    items=doc('.grid-item .grid-panel').items()
    i=0
    for item in items:
        i=i+1
        product={
                'image':item.find('.img').attr('data-src'),
                'price':item.find('.price').text(),
                'title':item.find('.product-title').attr('title'),
                'shop':item.find('.sale-row .week-sale').text()
                }
        if product.get('image')!=None:
            save_to_mongo(product)
            
import pymongo
#定义把商品信息存储到mongoDB的函数
client=pymongo.MongoClient(host="localhost",port=27017)
db=client.taobao
collection=db.foods
collection.drop()
def save_to_mongo(result):
    try:
        if collection.insert_one(result):
            print('存储到MongoDB成功')
    except:
        print('存储失败')

#主函数
if  __name__=="__main__":
    for i in range(1,100):
        index_page(i)


