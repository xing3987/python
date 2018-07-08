# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 23:09:45 2018

@author: Administrator
"""

from enum import Enum,unique

Month=Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul'))

#遍历枚举类型

for name,member in Month.__members__.items():
    print(name,'---',member,'---',member.value)
    
print(Month.Jan)
print('######################')
'''
可见，我们可以直接使用 Enum 来定义一个枚举类。上面的代码，我们创建了一个有关月份的
枚举类型 Month ，这里要注意的是构造参数，第一个参数 Month 表示的是该枚举类的类名，
第二个 tuple 参数，表示的是枚举类的值；当然，枚举类通过 __members__ 遍历它的所有成
员的方法。注意的一点是 ， member.value 是自动赋给成员的 int类型的常量，默认是从 1 
开始的。而且 Enum 的成员均为单例（Singleton），并且不可实例化，不可更改
'''


#自定义枚举类型的值

# @unique 装饰器可以帮助我们检查保证没有重复值
@unique
class Month(Enum):
    Jan = 'January'
    Feb = 'February'
    Mar = 'March'
    Apr = 'April'
    May = 'May'
    Jun = 'June'
    Jul = 'July'
    Aug = 'August'
    Sep = 'September '
    Oct = 'October'
    Nov = 'November'
    Dec = 'December'
    
if __name__=='__main__':
    print(Month.Jan,"---",Month.Jan.name,"---",Month.Jan.value)
    for name,member in Month.__members__.items():
        print(name,'---',member,'---',member.value)
    
    