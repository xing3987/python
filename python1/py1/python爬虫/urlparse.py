# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 23:10:36 2018

@author: Administrator
"""

import urllib

#urlparse()可以用来处理url的识别和分段,具体可以分成6部分(逆向方法为urlunparse)
#  协议，域名，路径，参数，查询条件，描点
print('--------urlprase()---------')
result=urllib.parse.urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result),result)
print(result.scheme,result.netloc,result[3],result[4])
#urllib.parse.urlparse(urlstring,scheme='',allow_fragments=True):三个参数url,协议，是否忽略锚点（描点部分合并到path）

#urlsplit()分隔url，参数部分合并到路径，其他同parse(逆向方法为urlunsplit)

result=urllib.parse.urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result)

data=['http','www.baidu.com','index.html','a=6','comment']
print(urllib.parse.urlunsplit(data))


#urljoin()使第二个参数对与第一个参数url合并，如果第一个参数（只有协议和域名生效）有的部分覆盖，没有的部分就加入

print(urllib.parse.urljoin('http://www.baidu.com','//www.qq.com?question=3'))


#常用方法urlencode(),使字典型参数序列化为get请求参数

params={'name':'germey','age':'22'}
base_url="http://www.baidu.com?"
url=base_url+urllib.parse.urlencode(params)
print(url)

#parse_qs()把get型参数反序列化成字典型

query='name=germey&age=22'
print(urllib.parse.parse_qs(query))

#parse_qsl()反序列化成元组型列表
print(urllib.parse.parse_qsl(query))

#quote()对url中带有的中文参数进行转url编码

keyword="大哥别杀我"
url='https://www.baidu.com/w?wd='+urllib.parse.quote(keyword)
print(url)

#反编码unquote()
print(urllib.parse.unquote(url))