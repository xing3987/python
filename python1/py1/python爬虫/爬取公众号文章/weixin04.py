# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 23:47:20 2018

@author: Administrator
"""

from weixin01 import RedisQueue,WeixinRequest
from weixin03 import MysqlWx
from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq
from requests import Session,ReadTimeout,ConnectionError

proxy_pool_url='http://127.0.0.1:7070/random'
max_failed_time=5
valid_statuses=[200]

class SpiderWx():
    base_url="http://weixin.sogou.com/weixin"
    keyword='101女团'
    headers={
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Connection':'keep-alive',
            'Cookie':'ABTEST=8|1535294251|v1; IPLOC=CN3205; SUID=25DD25993E18960A000000005B82BB2B; __guid=14337457.825266257461256600.1535294197572.036; SUID=25DD25992B12960A000000005B82BB2B; weixinIndexVisited=1; SUV=008D64129925DD255B82BB3C73FBF439; SNUID=39C038841D19694B936161FF1DCB7ADA; JSESSIONID=aaaSAbCTCtOlqh10h6Bvw; monitor_count=35; sct=5',
            'Host':'weixin.sogou.com',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
            }
    session=Session()
    queue=RedisQueue()
    mysql=MysqlWx()
    '''
    定义一个函数来获取随机代理
    使用自定义的代理池proxypool05
    端口为127.0.0.1:7070
    获取的代理连接为 /random
    !!本来所有的need_proxy=True,但是实测使用代理爬取失败，估计是获取的代理问题，所以这里就默认没有打开自动生成代理的程序
    '''     
    def get_proxy(self):
        try:
            response=requests.get(proxy_pool_url)
            if response.status_code==200:
                print('Get Proxy',response.text)
                return response.text
            return None
        except requests.ConnectionError:
            return None
    
    def start(self):
        #初始化
        self.session.headers.update(self.headers)
        start_url=self.base_url+'?'+urlencode({'type':2,'s_from':'input','query':self.keyword})
        weixin_request=WeixinRequest(url=start_url,callback=self.parse_index,need_proxy=True) #初始化callback为parse_index()函数
        #调度一个请求
        self.queue.add(weixin_request)
        
    def parse_index(self,response):
        #解析索引页的response,得到文章的链接
        doc=pq(response.text)
        items=doc('.txt-box h3 a').items()
        for item in items:
            url=item.attr('href')
            weixin_request=WeixinRequest(url=url,callback=self.parse_detail,need_proxy=True)  #得到需要请求的连接，将callback设置为parse_detail(),下回请求就使用该函数解析
            yield weixin_request
        next=doc('#sogou_next').attr('href')  #如果下一页的标签有链接
        if next:
            url=self.base_url+str(next) #得到下一页的链接
            weixin_request=WeixinRequest(url=url,callback=self.parse_index,need_proxy=True) #把请求加入请求池中
            yield weixin_request
            
    def parse_detail(self,response):
        #解析文章链接的response，得到详细信息
        doc=pq(response.text)
        data={
             'title':doc('.rich_media_title').text().replace(' ','').replace('\n',''),
             'content':doc('.rich_media_content').text().replace(' ','').replace('\n',''),  #去空格和换行符
             'date':doc('#publish_time').text().replace(' ','').replace('\n',''),
             'nickname':doc('#js_author_name').text().replace(' ','').replace('\n',''),
             'wechat':doc('#js_name').text().replace(' ','').replace('\n','')
                }
        yield data
        
    def request(self,weixin_request):
        #执行请求
        try:
            if weixin_request.need_proxy:   #如果需要代理
                proxy=self.get_proxy()
                if proxy:
                    proxies={
                            'http':'http://'+proxy,
                            'https':'https://'+proxy
                    }
                    #return self.session.send(weixin_request.prepare(),timeout=weixin_request.timeout,allow_redirects=False,proxies=proxies)
                    return requests.get(url=weixin_request.url,timeout=10,proxies=proxies)
             #使用Session的send()方法发送请求，同时设定重定向和超时 
            #return self.session.send(weixin_request.prepare(),timeout=weixin_request.timeout,allow_redirects=False)
            return requests.get(url=weixin_request.url,timeout=10)
        except (ConnectionError,ReadTimeout) as e:
            print(e.args)
            return False
        
    def error(self,weixin_request):
        #请求错误时的处理
        weixin_request.fail_time=weixin_request.fail_time+1
        print('Request Failed',weixin_request.fail_time,"Times",weixin_request.url)
        if weixin_request.fail_time<max_failed_time: #如果失败次数小于设定的最大次数，加入redis队列继续等待爬取
            self.queue.add(weixin_request)
            
    def schedule(self):
        #调度请求
        while not self.queue.empty():
            weixin_request=self.queue.pop()
            callback=weixin_request.callback #得到callback函数
            print('Schedule',weixin_request.url)
            response=self.request(weixin_request)
            if response and response.status_code in valid_statuses:
                results=list(callback(response))  #使用函数parse_index()或parse_detail()解析response
                if results:
                    for result in results:
                        print('New result',result)
                        if isinstance(result,WeixinRequest):  #如果请求返回response(parse_index)
                            self.queue.add(result)
                        if isinstance(result,dict):  #如果请求返回字典型数据(parse_detail)
                            self.mysql.insert('articles',result)
                else:
                    self.error(weixin_request)
            else:
                self.error(weixin_request)

    def run(self):
        self.start()
        self.schedule()
        
if __name__=='__main__':
    spider=SpiderWx()
    spider.run()
    '''
    response=requests.get('http://weixin.sogou.com/weixin?type=2&s_from=input&query=101%E5%A5%B3%E5%9B%A2',timeout=10)
    doc=pq(response.text)
    items=doc('.txt-box h3 a').items()
    for item in items:
        print('xx')
        url=item.attr('href')
        weixin_request=WeixinRequest(url=url,callback=spider.parse_detail,need_proxy=False)  #得到需要请求的连接，将callback设置为parse_detail(),下回请求就使用该函数解析
        print(weixin_request)'''
                
    
    
            
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        