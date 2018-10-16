# -*- coding: utf-8 -*-
import scrapy

'''
主页：  https://m.weibo.cn/api/container/getIndex?uid={uid}&type=uid&value={uid}&containerid=100505{uid}
关注页：https://m.weibo.cn/api/container/getIndex?containerid=231051_-_followers_-_{uid}&page={page}
粉丝页：https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_{uid}&page={page}
微博列表：https://m.weibo.cn/api/container/getIndex?uid={uid}&type=uid&page={page}&containerid=107603{uid}
'''
from scrapyweibo.items import UserItem,UserRelationItem,WeiboItem
import json

class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['m.weibo.cn']
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
                
        #关注
        uid=user_info.get('id')
        yield scrapy.Request(url=self.follow_url.format(uid=uid,page=1),headers=self.headers,callback=self.parse_follows,meta={'page':1,'uid':uid})
        #粉丝
        yield scrapy.Request(url=self.fan_url.format(uid=uid,page=1),headers=self.headers,callback=self.parse_fans,meta={'page':1,'uid':uid})
        #微博
        yield scrapy.Request(url=self.weibo_url.format(uid=uid,page=1),headers=self.headers,callback=self.parse_weibos,meta={'page':1,'uid':uid})
        
    def parse_follows(self,response):
        result=json.loads(response.text)
        if result.get('ok') and result.get('data').get('cards') and len(result.get('data').get('cards')) and result.get('data').get('cards')[-1].get('card_group'):
            follows=result.get('data').get('cards')[-1].get('card_group')
            for follow in follows:
                if follow.get('user'):
                    uid=follow.get('user').get('id')
                    yield scrapy.Request(url=self.user_url.format(uid=uid),headers=self.headers,callback=self.parse_user)
                
                #关注列表
                uid=response.meta.get('uid')
                user_relation_item=UserRelationItem()
                all_follows=[{'id':follow.get('user').get('id'),'name':follow.get('user').get('screen_name')} for follow in follows]
                user_relation_item['id']=uid
                user_relation_item['follows']=all_follows
                user_relation_item['fans']=[]
                yield user_relation_item
                #下一页关注
                page=response.meta.get('page')+1
                yield scrapy.Request(url=self.follow_url.format(uid=uid,page=page),headers=self.headers,callback=self.parse_follows,meta={'page':page,'uid':uid})
                
    def parse_fans(self,response):
        result=json.loads(response.text)
        if result.get('ok') and result.get('data').get('cards') and len(result.get('data').get('cards')) and result.get('data').get('cards')[-1].get('card_group'):
            follows=result.get('data').get('cards')[-1].get('card_group')
            for follow in follows:
                if follow.get('user'):
                    uid=follow.get('user').get('id')
                    yield scrapy.Request(url=self.user_url.format(uid=uid),headers=self.headers,callback=self.parse_user)
                
                #关注列表
                uid=response.meta.get('uid')
                user_relation_item=UserRelationItem()
                all_fans=[{'id':follow.get('user').get('id'),'name':follow.get('user').get('screen_name')} for follow in follows]
                user_relation_item['id']=uid
                user_relation_item['follows']=[]
                user_relation_item['fans']=all_fans
                yield user_relation_item
                #下一页关注
                page=response.meta.get('page')+1
                yield scrapy.Request(url=self.follow_url.format(uid=uid,page=page),headers=self.headers,callback=self.parse_follows,meta={'page':page,'uid':uid})
            
    #爬取微博主页的具体内容
    def parse_weibos(self,response):
        result=json.loads(response.text)
        if result.get('ok') and result.get('data').get('cards'):
            weibos=result.get('data').get('cards')
            for weibo in weibos:
                mblog=weibo.get('mblog')
                if mblog:
                    weibo_item=WeiboItem()
                    field_map={
                            'id':'id',
                            'attitudes_count':'attitudes_count',
                            'comments_count':'comments_count',
                            'reposts_count':'reposts_count',
                            'picture':'original_pic',
                            'pictures':'pics',
                            'source':'source',
                            'text':'text',
                            'raw_text':'raw_text',
                            'thumbnail':'thumbnail_pic',
                            'created_at':'created_at'
                            }
                    for field,attr in field_map.items():
                        weibo_item[field]=mblog.get(attr)
                        weibo_item['user']=response.meta.get('uid')
                        yield weibo_item
                
                #下一页微博
                uid=response.meta.get('uid')
                page=response.meta.get('page')+1
                yield scrapy.Request(url=self.weibo_url.format(uid=uid,page=page),headers=self.headers,callback=self.parse_weibos,meta={'page':page,'uid':uid})
                        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
