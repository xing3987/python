# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 23:12:04 2018

@author: Administrator
"""
#首先有这么一个输出员工打卡信息的函数：

def punch():
    print('昵称：小王  部门：工程部 上班打卡成功')
punch()


import time
def punch1():
    print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
    print('昵称：小王  部门：工程部 上班打卡成功')
punch1()

print('#########punch1##############')
      
def punch2():
    print('昵称：小王  部门：工程部 上班打卡成功')

def add_time(func):
    print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
    func()
add_time(punch2)

print('##########punch2#############')

def punch3():
    print('昵称：小王  部门：工程部 上班打卡成功')


def add_time(func):
    print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
    func()


def holiday():
    print('天气太冷，今天放假')


add_time(punch3)
add_time(holiday)
print('########punch3###############')
'''
天气太冷，今天放假
使用函数编程是不是很方便，但是，我们每次调用的时候，我们都不得不把原来的函数作为参数传递进去，还能不能有更好的实现方式呢？有的，就是本文要介绍的装饰器，因为装饰器的写法其实跟闭包是差不多的，不过没有了自由变量，那么这里直接给出上面那段代码的装饰器写法，来对比一下，装饰器的写法和函数式编程有啥不同。
'''

def decorator(func):
    def punch4():
        print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
        func()
    return punch4


def punch4():
    print('昵称：小王  部门：工程部 上班打卡成功')

f = decorator(punch4)
f()
print('#########punch4##############')
'''

通过代码，能知道装饰器函数一般做这三件事：

接收一个函数作为参数
嵌套一个包装函数, 包装函数会接收原函数的相同参数，并执行原函数，且还会执行附加功能
返回嵌套函数
可是，认真一看这代码，这装饰器的写法怎么比函数式编程还麻烦啊。而且看起来比较复杂，甚至有点多此一举的感觉。

那是因为我们还没有用到装饰器的 “语法糖” ，我们看上面的代码可以知道， Python 在引入装饰器 （Decorator） 的时候，没有引入任何新的语法特性，都是基于函数的语法特性。这也就说明了装饰器不是 Python 特有的，而是每个语言通用的一种编程思想。只不过 Python 设计出了 @ 语法糖，让 定义装饰器，把装饰器调用原函数再把结果赋值为原函数的对象名的过程变得更加简单，方便，易操作，所以 Python 装饰器的核心可以说就是它的语法糖。

那么怎么使用它的语法糖呢？很简单，根据上面的写法写完装饰器函数后，直接在原来的函数上加 @ 和装饰器的函数名。如下：
'''


def decorator2(func):
    def punch5():
        print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
        func()

    return punch5

@decorator2
def punch5():
    print('昵称：小王  部门：工程部 上班打卡成功')

punch5()
print('#########punch5##############')
'''
那么这就很方便了，方便在我们的调用上，比如例子中的，使用了装饰器后，直接在原本的函数上加上装饰器的语法糖就可以了，本函数也无虚任何改变，调用的地方也不需修改。

不过这里一直有个问题，就是输出打卡信息的是固定的，那么我们需要通过参数来传递，装饰器该怎么写呢？装饰器中的函数可以使用 *args 可变参数，可是仅仅使用 *args 是不能完全包括所有参数的情况，比如关键字参数就不能了，为了能兼容关键字参数，我们还需要加上 **kwargs 。

因此，装饰器的最终形式可以写成这样：
'''


def decorator3(func):
    def punch6(*args, **kwargs):
        print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
        func(*args, **kwargs)
    return punch6


@decorator3
def punch6(name, department):
    print('昵称：{0}  部门：{1} 上班打卡成功'.format(name, department))


@decorator3
def print_args(reason, **kwargs):
    print(reason)
    print(kwargs)


punch6('小王', '业务部')
print_args('小王', sex='男', age=20)
