# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 18:12:02 2018

@author: Administrator
"""


import requests


headers={
        'Cookie':'_octo=GH1.1.504639994.1531043286; logged_in=yes; dotcom_user=xing3987; _gat=1; _ga=GA1.2.1984624114.1531043286',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        }

r=requests.get('https://baiduyunbo.com/d7202a78-c500-4abe-940c-627e87f4c7c8',headers=headers)

with open('x1.mp4','wb') as f:
    f.write(r.content)