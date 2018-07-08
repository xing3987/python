# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 17:24:12 2018

@author: Administrator
"""

'''
例：
爬取知乎的今日最热疑问
'''
import re
import requests
#模拟头部防止被屏蔽，参考robots.txt文档模拟
'''
正则
.表示任意字符
.?表示尽可能少的匹配（非贪婪型）
.*?表示一个匹配以后，就往下进行，所以不会进行回溯，具有最小匹配的性质
'''
headers={
        'User-Agent':'Mozilla/5.0(Macintosh;Intel Mac OS X 10_11_4) AppleWebKit/537.36(KHTML,like Gecko) Chrome/52.0.2743.116 Safari/537.36'
        }
r=requests.get('https://www.zhihu.com/explore',headers=headers)
pattern=re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)  #explore-feed是最上层classname,question_link是第二层classname,(.*?)为分组查询得到的内容
titles=re.findall(pattern,r.text)

for i in range(len(titles)):
    print(titles[i])
    
    

#抓取二进制数据如：图片等

r=requests.get('https://github.com/favicon.ico')
#print(r.text) #二进制数据转成str类型输出产生乱码
print(r.content)

with open('favicon.ico','wb') as f:
    f.write(r.content)
    
r.close()