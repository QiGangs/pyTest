#!/usr/bin/python
# -*- coding: UTF-8 -*-
from PIL import Image


im = Image.open('/Users/qigang/Desktop/test.jpg')
# 获得图像尺寸:
#w, h = im.size
# 缩放到50%:
#im.thumbnail((w/5, h/5))
# 把缩放后的图像用jpeg格式保存:
im.save('/Users/qigang/Desktop/test1.png', 'png')


print im.format, im.size, im.mode
#im.show()