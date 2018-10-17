# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class ScrapyweiboSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


import requests

class ProxyMiddleware(object):
    
    def __init__(self,proxy_url):
        self.proxy_url=proxy_url

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        return cls(
                proxy_url=crawler.settings.get('PROXY_URL')
                )
        
    def get_random_proxy(self):
        try:
            response=requests.get(self.proxy_url)
            if response.status_code==200:
                proxy=response.text
                return proxy
        except requests.ConnectionError:
            return False
        
    #主方法(入口)
    def process_request(self,request,spider):
        if request.meta.get('download_timeout'): #判断是否爬取失败
            proxy=self.get_random_proxy()
            print('使用代理：'+proxy)
            if proxy:
                uri='https://{proxy}'.format(proxy=proxy)
                request.meta['proxy']=uri  #把request的代理设置为uri


    
