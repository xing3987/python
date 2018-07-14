# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 22:54:57 2018

@author: Administrator
"""
import requests
import re
import json


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
#1.排名，2.图片，3.电影名称，4.主演，5.上映时间，6.评分    
pattern=re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src'+
                   '="(.*?)".*?name"><.*?>(.*?)</a>.*?star">(.*?)</p>'+
                   '.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>',re.S)


#定义方法，得到数据并生成字典
def parse_one_page(html):
    items=re.findall(pattern,html)
    for item in items:
        yield{
            'index':item[0],
            'image':item[1],
            'title':item[2].strip(),
            'actor':item[3].strip(),
            'time':item[4].strip(),
            'score':item[5].strip()+item[6].strip()
                }

#定义写入文件,并保存成json格式的函数
def write_to_file(content):
    with open('电影排行.txt','a',encoding='utf-8') as f:
        #print(type(json.dumps(content)))
        f.write(json.dumps(content,ensure_ascii=False)+'\n')  #json.dumps()实现字典序列化,ensure_ascii输出为中文
        f.close()
        
        
#定义爬取一页页面的方法        
def main(offset):
    url='http://maoyan.com/board/4?offset='+str(offset)
    html=get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item)

#运行主程序
if __name__=='__main__': 
    print('开始爬取...')
    for i in range(10):
        main(offset=i*10)
    print('爬取完毕...')
    
    

    
    
    
    
    
    
    
    
    
    


