# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 00:01:52 2018

@author: Administrator
"""

import requests
from lxml import etree  #具体用法参照xpath

class Login():
    def __init__(self):
        self.headers={
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
                'Host':'github.com',
                'Referer':'https://github.com/login'
                }
        self.login_url='https://github.com/login'
        self.post_url='https://github.com/session'  
        self.logined_url='https://github.com/settings/profile'
        self.session=requests.Session()  #使用Session来保持持续的登陆状态
        
    def token(self): #获得authenticity_token值
        response = self.session.get(url=self.login_url, headers=self.headers)
        selector=etree.HTML(response.text)
        token=selector.xpath('//div//input[2]/@value')[0] #直接得到的是一个集合，使用下标得到每一个数
        return token
    

    #通过查看https://github.com/login页面的form表单input的name得到要提交的数据
    #查看form表单action="/session"  得到提交到的连接地址'https://github.com/session'
    def login(self, email, password):
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.token(),
            'login': email,
            'password': password
        }
        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        if response.status_code == 200:
            self.dynamics(response.text)
        
        response = self.session.get(self.logined_url, headers=self.headers)
        if response.status_code == 200:
            self.profile(response.text)
            
    def dynamics(self,html):
        #得到所有的动态信息
        selector=etree.HTML(html)
        dynamics=selector.xpath('//div[contains(@class,"news")]//div[contains(@class,"alert")]')
        for item in dynamics:
            dynamic=' '.join(item.xpath('.//div[@class="title"]//text()')).strip()
            print(dynamic)
        
    def profile(self,html):
        selector=etree.HTML(html)
        name=selector.xpath('//input[@id="user_profile_name"]/@value')[0]
        email=selector.xpath('//select[@id="user_profile_email"]//option[@selected="selected"]/text()')[0]
        print(name,email)
        
if __name__ == "__main__":
    login = Login()
    login.login(email='**********',password='*******')  #登陆的帐号密码
     
        
    