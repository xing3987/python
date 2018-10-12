# -*- coding: utf-8 -*-
import scrapy

'''
主页：  https://m.weibo.cn/api/container/getIndex?uid={uid}&type=uid&value={uid}&containerid=100505{uid}
关注页：https://m.weibo.cn/api/container/getIndex?containerid=231051_-_followers_-_{uid}&page={page}
粉丝页：https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_{uid}&page={page}
微博列表：https://m.weibo.cn/api/container/getIndex?uid={uid}&type=uid&page={page}&containerid=107603{uid}
'''
from scrapyweibo.items import UserItem
import json

class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['weibo.com']
    user_url="https://m.weibo.cn/api/container/getIndex?uid={uid}&type=uid&value={uid}&containerid=100505{uid}"
    follow_url='https://m.weibo.cn/api/container/getIndex?containerid=231051_-_followers_-_{uid}&page={page}'
    fan_url='https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_{uid}&page={page}'
    weibo_url='https://m.weibo.cn/api/container/getIndex?uid={uid}&type=uid&page={page}&containerid=107603{uid}'
    
    headers={
            'content-type':'text/html;charset=utf-8',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'Cookie':'SINAGLOBAL=4587561981028.947.1539012563123; un=18606207041; wvr=6; TC-Page-G0=c9fb286cd873ae77f97ce98d19abfb61; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhgxU6e2UpsoOcWZvrEH2kF5JpX5KMhUgL.FoeESo2Xe02feh22dJLoIfQLxKnLB-qLBoMLxKBLB.qLB--LxKqL1KBLBo.LxKBLB.BLBK5LxKMLB.zL1K2LxK-LB--L1-2LxKML1-2L1hBLxKqL1h.L12zLxKqL1-eLB.2LxK-L12qLBoMt; ALF=1570631796; SSOLoginState=1539095797; SCF=AiZmJgE-UPstvf2xt8L9d6yHZK8OovHLNjcaUVyWJha8FNBxpKOcYl_MdoDGxpOgqm3mYpKzifQXYe0Nj_NsEHc.; SUB=_2A252uMylDeRhGeVM7VMV8y_Jyz2IHXVVz7ltrDV8PUNbmtAKLRiikW9NTLceETuS40gBQLdXTtkDK81c3GxlGvkS; SUHB=0auw9VG1IvMvYj; TC-V5-G0=52dad2141fc02c292fc30606953e43ef; TC-Ugrow-G0=370f21725a3b0b57d0baaf8dd6f16a18; _s_tentry=weibo.com; Apache=6156855025714.1455.1539095740208; ULV=1539095740438:2:2:2:6156855025714.1455.1539095740208:1539012563129'
            }

    start_users=['1784537661','3261134763','3952070245']  #从几个大V开始爬取
    
    def start_requests(self):
        for uid in self.start_users:
            url=self.user_url.format(uid=uid)
            yield scrapy.Request(url=url,headers=self.headers,callback=self.parse_user)
            
    def parse_user(self,response):
        result=json.loads(response.text)
        user_info=result.get('data').get('userInfo')
        field_map={
                    'id':'id',
                    'name':'screen_name',
                    'avatar':'profile_image_url',
                    'cover':'cover_image_phone',
                    'description':'description',
                    'gender':'gender',
                    'follows_count':'follow_count',
                    'fans_count':'followers_count',
                    'weibos_count':'statuses_count'
                }
        user_item=UserItem()
        for field,attr in field_map.items():
            user_item[field]=user_info.get(attr)
        yield user_item
