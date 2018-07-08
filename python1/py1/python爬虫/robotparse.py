# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 00:06:52 2018

@author: Administrator
"""
'''
网站的robots.txt的文件可以设置网页是否可以爬取的权限，使用robotparser解析
set_url():设置robots.txt文件的链接
read():读取robots.txt文件
parse()：解析robots.txt文件
can_fetch():判断是否可以被爬去传入两个参数user-agent,url返回true,false
mtime():返回删除抓取和分析robots.txt文件时间
modified()：将当前时间设置成上次抓取和分析robot.txt的时间
'''
from urllib.robotparser import RobotFileParser

rp=RobotFileParser("http://www.jianshu.com/robots.txt")
print(rp.can_fetch('*','http://www.jianshu.com/pb6755'))
