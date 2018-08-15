# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 22:03:30 2018

@author: Administrator
"""

import tesserocr
from PIL import Image

image=Image.open('image/code.jpg')
result=tesserocr.image_to_text(image)
print(result)

print(tesserocr.file_to_text('image/code.jpg')) #将文件转为字符(识别效果较差)

'''
为了加强图像的识别度，进行灰度处理
'''
image=Image.open('image/code.jpg')
image=image.convert('L')  #该方法将图像转换成灰度图像
#image.show() #查看图片
result=tesserocr.image_to_text(image)
print(result)

image=Image.open('image/code.jpg')
image=image.convert('1')  #传入参数1将图像进行二值化处理
#image.show()
result=tesserocr.image_to_text(image)
print(result)

print('------------------------')

image=Image.open('image/code.jpg')
image=image.convert('L') 
table=[]
for i in range(256):
    if i<127:
        table.append(0)
    else:
        table.append(1)
image=image.point(table,'1')
image.show()
result=tesserocr.image_to_text(image)
print(result)
























