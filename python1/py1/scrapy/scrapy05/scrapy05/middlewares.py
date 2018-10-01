# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class Scrapy05SpiderMiddleware(object):
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



from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from scrapy.http import HtmlResponse
from logging import getLogger

class SeleniumDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    def __init__(self,timeout):  #可以不在这里赋值直接写timeout可以加service_args参数
        self.logger=getLogger(__name__)
        self.timeout=timeout
        self.browser=webdriver.Chrome()
        self.browser.set_window_size(1400,700)
        self.browser.set_page_load_timeout(self.timeout)
        self.wait=WebDriverWait(self.browser,self.timeout)
        
    def __del__(self):
        self.browser.close()

    @classmethod
    def from_crawler(cls, crawler):  #给前面的参数赋值，得到settings里的值
        # This method is used by Scrapy to create your spiders.
        return cls(
                timeout=crawler.settings.get('SELENIUM_TIMEOUT'),
                )

    def process_request(self, request, spider):
        '''
        用PhantomJs抓取页面
        :param request:Request对象
        ：param spider;Spider对象
        ：return:HtmlResponse
        '''
        self.logger.debug('****************PhantomJS is starting******************')
        page=request.meta.get('page',1)  #得到meta传递来的参数，默认为1
        try:
            self.logger.debug('******start try********'+request.url)
            self.browser.get(request.url)
            self.logger.debug('******start try2********')
            if page>1:
                input=self.wait.until(EC.presence_of_element_located((
                        By.CSS_SELECTOR,'#spulist-pager div.form>input.input.J_Input')))
                submit=self.wait.until(EC.element_to_be_clickable((
                        By.CSS_SELECTOR,'#spulist-pager div.form>span.btn.J_Submit')))
                input.clear()
                #print(input,submit)
                input.send_keys(page)
                submit.click()
            
            self.wait.until(EC.presence_of_element_located((
                    By.CSS_SELECTOR,'.grid-item .grid-panel'))) #等待直到css选择的东西加载完毕
            self.wait.until(EC.text_to_be_present_in_element((
                    By.CSS_SELECTOR,'#spulist-pager .item.active>span'),str(page)))  
            self.logger.debug('******start send response*********')
            return HtmlResponse(url=request.url,body=self.browser.page_source,request=request,encoding='utf-8',status=200)  #爬取结束后返回页面body内容
            self.logger.debug('******end response*********')
        except TimeoutException:
            self.logger.debug('******except*********')
            return HtmlResponse(url=request.url,request=request,status=500)  #爬取失败返回失败的状态码
        
    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)    
        
        
        
        
        
        
        
        
        
        
        
        


