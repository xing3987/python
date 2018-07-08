# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 22:47:52 2018

@author: Administrator
"""
'''
python正则表达式 re （二）compile
re正则表达式模块还包括一些有用的操作正则表达式的函数。下面主要介绍compile函数。 
定义： 
compile(pattern[,flags] ) 根据包含正则表达式的字符串创建模式对象。

通过python的help函数查看compile含义：

help(re.compile)
compile(pattern, flags=0) 
Compile a regular expression pattern, returning a pattern object.

通过help可以看到compile方法的介绍，返回一个pattern对象，但是却没有对第二个参数flags进行介绍。第二个参数flags是匹配模式，可以使用按位或’|’表示同时生效，也可以在正则表达式字符串中指定。Pattern对象是不能直接实例化的，只能通过compile方法得到。匹配模式有： 
1).re.I(re.IGNORECASE): 忽略大小写 
2).re.M(MULTILINE): 多行模式，改变’^’和’$’的行为 
3).re.S(DOTALL): 点任意匹配模式，改变’.’的行为 
4).re.L(LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定 
5).re.U(UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性 
6).re.X(VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释

例如： 
pattern1 = re.compile(r”“”\d + #整数部分 
. #小数点 
\d * #小数部分”“”, re.X) 
这里正则表达式为三个”号引起来的多行字符串，则将匹配模式设置为re.X 可以多行匹配。

函数re.compile将正则表达式（以字符串书写的）转换为模式对象，可以实现更加有效的匹配。例子：
import re
text = "JGood is a handsome boy, he is cool, clever, and so on..."
re.findall(r'\w*oo\w*', text)    #查找所有包含'oo'的单词

使用compile函数： 
导入re模块： 
import re 
text = “JGood is a handsome boy, he is cool, clever, and so on…” 
regex = re.compile(r’\w*oo\w*’) 
print regex.findall(text) #查找所有包含’oo’的单词
'''