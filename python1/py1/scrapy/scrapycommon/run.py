# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 23:33:17 2018

@author: Administrator
"""
#创建启动方法


import sys
from scrapy.utils.project import get_project_settings
from scrapycommon.utils import get_config
from scrapy.crawler import CrawlerProcess

def run():  #创建启动接口
    name=sys.argv[1]  #得到外部输入的第一个数sys.argv[0]为本身
    custom_settings=get_config(name)
    spider=custom_settings.get('spider')
    project_settings=get_project_settings()  #得到当前project的通用设置
    settings=dict(project_settings.copy())   #复制当前配置
    settings.update(custom_settings.get('settings')) #合并配置里的setting和当前的通用设置
    process=CrawlerProcess(settings) #使用合并后的设置
    process.crawl(spider,**{'name':name})  #设置启动命令，给name赋值
    process.start()
    
if __name__=='__main__':
    run()
    