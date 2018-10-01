# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import quote
from scrapy06.items import ProductItem
from scrapy_splash import SplashRequest
from pyquery import PyQuery as pq
'''
对接splash爬取淘宝数据,选择器使用querySelector，该选择器使用方法同css
'''
script='''
function main(splash,args)
    splash.image_enabled=false
    assert(splash:go(args.url))
    assert(splash:wait(args.wait))
    js=string.format("document.querySelector('#mainsrp-pager div.form>input').value=%d;document.querySelector('#mainsrp-pager div.form>span.btn.J_Submit').click()",args.page)
    splash:evaljs(js)
    assert(splash:wait(args.wait))
    return splash:html()
end
    '''
class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['www.taobao.com']
    base_url = 'https://s.taobao.com/search?q='
    
    def start_requests(self):
        keyword = self.settings.get('KEYWORDS')
        for page in range(1,self.settings.get('MAX_PAGE')+1):
            url=self.base_url+quote(keyword)
            print('*********************'+url)
            yield SplashRequest(url=url,callback=self.parse,endpoint='execute',args={'lua_source':script,'page':page,'wait':7}) #使用execute接口传递splash请求
    
    def parse(self, response):
        print('////////start parse///////////')
        doc=pq(response.text)
        products=doc('.grid-item .grid-panel').items()
        for product in products:
            item=ProductItem()
            item['image']=product.find('.img').attr('data-src')
            item['price']=product.find('.price').text()
            item['title']=product.find('.product-title').attr('title')
            item['shop']=product.find('.sale-row .week-sale').text()
            yield item
