# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 16:06:28 2018

@author: Administrator
"""

from pyquery import PyQuery as pq

import requests
def get_page(url):
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

class ProxyMetaclass(type):
    def __new__(cls,name,bases,attrs):
        count=0
        attrs['__CrawlFunc__']=[]
        for k,v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count+=1
        attrs['__CrawlFuncCount__']=count
        return type.__new__(cls,name,bases,attrs)
    
class Crawler(object,metaclass=ProxyMetaclass):
    def get_proxies(self,callback):
        proxies=[]
        for proxy in eval("self.{}()".format(callback)):  
            print('getproxy:',proxy)
            proxies.append(proxy)
        return proxies
                
    def crawl_daili66(self,page_count=4): 
        start_url='http://www.66ip.cn/{}.html'
        urls=[start_url.format(page) for page in range(1,page_count+1)]
        for url in urls:
            #print('Crawling',url)
            html=get_page(url)
            if html:
                doc=pq(html)
                trs=doc('.containerbox table tr:gt(0)').items() 
                for tr in trs:
                    ip=tr.find('td:nth-child(1)').text()
                    port=tr.find('td:nth-child(2)').text()
                    #print(ip,port)
                    yield ':'.join([ip,port])
        
    def crawl_proxy360(self):
        start_url='http://www.goubanjia.com/'
        html=get_page(start_url)
        if html:
            doc=pq(html)
            tds=doc('td.ip').items()
            for td in tds:
                td.find('p').remove()
                yield td.text().replace(' ','').replace("\n", "")
