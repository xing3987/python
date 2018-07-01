# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 23:18:19 2018

@author: Administrator
"""

import re
from utiltool import blocks

f0=open('test_input.txt','r')
f1=open('output.html','w')

f1.write('<html><head><title>...</title><body>')



if __name__=='__main__':
    title=True
    for block in blocks(f0):
        block=re.sub(r'\*(.+?)\*',r'<em>\1</em>',block)  #\1表示匹配到的第一组
        if title:
            f1.write('<h1>')
            f1.write(block)
            f1.write('</h1>')
            title=False
        else:
            f1.write('<p>')
            f1.write(block)
            f1.write('</p>')
            
    f1.write('</body></html>')
    
f1.close()
f0.close()

