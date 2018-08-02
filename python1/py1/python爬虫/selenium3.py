# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 19:45:24 2018

@author: Administrator
"""

'''
动作链
'''
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

browser=webdriver.Chrome()
browser.get('http://www.runoob.com/try/try.php?filename=jqueryui-example-droppable')

#跳转到frame中，后面为id（默认frame是widow，如果要操作子frame要进入frame）,跳转回父类的frame:switch_to.parent_frame()
browser.switch_to.frame('iframeResult')  
source=browser.find_element_by_id('draggable')
target=browser.find_element_by_id('droppable')

actions=ActionChains(browser) #创建动作对象
actions.drag_and_drop(source,target) #创建动作内容(拖放)
actions.perform() #执行动作
time.sleep(5)
browser.close()

#执行js

browser=webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
#time.sleep(5)
browser.implicitly_wait(5)  #隐式等待,如果没找到节点等待固定时间，没有才抛出异常
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)') #执行js代码（括号中）
#browser.execute_script('alert("to buttom")')


#其他属性和定位
logo=browser.find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.get_attribute('class'))  #输出属性
print(logo.text) #输出节点文本内容
print(logo.id)
print(logo.location)  #节点位置
print(logo.tag_name)  #标签名
print(logo.size) #大小

#前进和后退
browser.get('http://www.baidu.com')
time.sleep(2)
browser.get('https://www.zhihu.com/explore')
time.sleep(2)
browser.back()  #后退
time.sleep(2)
browser.forward() #前进


#cookies管理
print(browser.get_cookies()) #获得所有cookie
browser.add_cookie({'name':'tom','domain':'www.zhihu.com','value':'germey'})  #增加cookie
print(browser.get_cookies())
browser.delete_all_cookies() #删除所有cookies
print(browser.get_cookies())


#选项卡管理
browser.execute_script('window.open()')  #执行js语句,打开一个窗口
print(browser.window_handles) #输出窗口
browser.switch_to_window(browser.window_handles[1]) #切换到第二个窗口
browser.get('http://www.taobao.com') 
time.sleep(2)
browser.switch_to_window(browser.window_handles[0]) #切换回第一个窗口
browser.get('https://python.org')

#异常处理
try:    
    browser.find_element_by_id('hello') #如果没有该id的节点会抛出异常
except:
    print('no such element')
    browser.close()

time.sleep(2)
browser.close()


















