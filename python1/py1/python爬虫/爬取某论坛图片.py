# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 00:16:13 2018

@author: Administrator

'''
先在本地创建文件夹用于储存图片数据(默认G:/image/)
url为某论坛地址
'''
"""
import re
import requests
import sys
#编写抓取页面的函数
def get_one_page(url):
    try:
        headers={
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'           
                }
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.text
        return None
    except:
        return None
 
#编写正则表达式:需要提取
pattern=re.compile('<img.*?class="zoom".*?src="(.*?)"',re.S)

#定义方法，得到数据并生成字典
def parse_one_page(html):
    items=re.findall(pattern,html)
    for item in items:
        yield(item)
        
#定义根据url提取并保存图片方法 
num=9660
def save_page(url):
    try:
        r=requests.get(url,timeout=1) #设置超时跳过
#        formatImg=url[-3:]  #截取图片最后三位，确定图片格式
        global num
        with open('G:/image/%s.jpg' %num,'wb') as fb:  #创建一个目标文件(wb比特写入模式,注意文件夹一定要有)
            print(sys.getsizeof(r.content))
            if sys.getsizeof(r.content)>200000:  #判断图片大小，如果太小则不保存
                fb.write(r.content)  #写入图片byte数据
                print('正在下载第%s张图片' %num)
                num=num+1           
        r.close()    
        fb.close()
    except BaseException as msg:
        print('保存出错，请确认url地址：'+url,msg)
    
    
#运行主程序
if __name__=='__main__': 
    print('开始爬取...')
    for i in range(1242066,1300000):
        url='http://*******/**-'+str(i)+'**.html'
        html=get_one_page(url)
        print(url)
        if type(html)==str:
            for item in parse_one_page(html):
                print(item)
                save_page(str(item))
    print('爬取完毕...')