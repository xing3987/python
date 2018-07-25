# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 22:33:47 2018

@author: Administrator
"""

'''
ajax爬取今日头条街拍美图，换params的keyword属性可以下载不同的数据
'''

import requests
from urllib.parse import urlencode

#定义一个函数通过传入hearders,url和params得到网页json数据
def get_page_jrtt(offset):
    headers={
            'x-requested-with':'XMLHttpRequest',
            'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
            }
    
    params={
            'offset':offset,
            'format':'json',
            'keyword':'街拍',
            'autoload':'true',
            'count':'20',
            'cur_tab':'1',
            'from':'search_tab'
            }
    url='https://www.toutiao.com/search_content/?'+urlencode(params)
    try:
        response=requests.get(url,headers=headers,timeout=3)
        if response.status_code==200:
            return response.json()
    except:
        return None
    
    
#定义取得json中的图片和标题的方法
def get_images_jrtt(json):
    for item in json.get('data'):
        title=item.get('title')
        images=item.get('image_list')
        if(images!=None):
            for image in images:
                yield{
                     'title':title,
                     'image':image.get('url')
                     }
                
#定义保存图片的方法
import os
from hashlib import md5
def save_image_jrtt(item):
    if not os.path.exists('image/'+item.get('title')):
        os.mkdir('image/'+item.get('title'))
    try:
        url='http:'+item.get('image')
        response=requests.get(url,timeout=3)
        file_path='image/'+'{0}/{1}.{2}'.format(item.get('title'),md5(response.content).hexdigest(),'jpg')
        if response.status_code==200:
            with open(file_path,'wb') as f:
                f.write(response.content)
        else:
            print('Already Download',file_path)
    except:
        print('Failed to save image')
        
#定义主函数，加入偏移数offset,使用线程池下载
from multiprocessing.pool import Pool

def main(offset):
    json=get_page_jrtt(offset)
    for item in get_images_jrtt(json):
        save_image_jrtt(item)

#起始，结束页
start=0
end=20

if __name__=='__main__':
    print('开始下载图片,请稍等..')
    pool=Pool()
    groups=([x*20 for x in range(start,end)])
    pool.map(main,groups)  #创建线程池，参数为函数名和传入参数
    pool.close()
    pool.join()   #调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    print('图片下载完成.')







