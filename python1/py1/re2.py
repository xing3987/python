# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 23:38:17 2018

@author: Administrator
"""
'''
re.match 和 re.search
re.match 函数

语法：

re.match(pattern, string, flags=0)
re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match() 就返回 none。

re.search 函数

语法：

re.search(pattern, string, flags=0)
re.search 扫描整个字符串并返回第一个成功的匹配。

re.match 和 re.search 的参数，基本一致的，具体描述如下：

参数	描述
pattern	匹配的正则表达式
string	要匹配的字符串
flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写
那么它们之间有什么区别呢？

re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回 None；而 re.search 匹配整个字符串，直到找到一个匹配。这就是它们之间的区别了。

re.match 和 re.search 在网上有很多详细的介绍了，可是再个人的使用中，还是喜欢使用 re.findall

看下下面的实例，可以对比下 re.search 和 re.findall 的区别，还有多分组的使用。具体看下注释，对比一下输出的结果：
'''
#group(0)表示字符串本身，group(1)表示正则表达式()中匹配到的第一个字符串---

import re

a = '<img src="https://s-media-cache-ak0.pinimg.com/originals/a8/c4/9e/a8c49ef606e0e1f3ee39a7b219b5c05e.jpg">'
# 使用 re.search
search=re.search('<img src="(.*)">',a)
print(search.group(0))
print(search.group(1))

# 使用 re.findall得到字符串数组
findall=re.findall('<img src="(.*)">',a)
print(findall)
print(findall[0])

# 多个分组的使用（比如我们需要提取 img 字段和图片地址字段）
re_search = re.search('<(.*) src="(.*)">', a)

# 打印 img
print(re_search.group(1))
# 打印图片地址
print(re_search.group(2))
# 打印 img 和图片地址，以元祖的形式
print(re_search.group(1, 2))
# 或者使用 groups
print(re_search.groups())














