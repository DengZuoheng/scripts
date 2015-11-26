#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import Image
def is_pic(extension):
    return extension.lower() in ['jpg','png','jpeg','gif','tif','bmp']

filename_list = os.listdir(os.getcwd())
sc16x9 = float(16)/float(9)
sc16x10 = float(16)/float(10)
for item in filename_list:
    path = os.path.join(os.getcwd(),item)
    if os.path.isdir(path):
        continue
    extension = os.path.splitext(item)[1][1:]
    if False == is_pic(extension):
        continue
    im = Image.open(item)
    width,height = im.size
    del im
    scale = float(width)/float(height)
    if sc16x10 - 0.01 <= scale <= sc16x9 + 0.01:
        if width >=1920 -2 and height >= 1080 -2:
            #statinfo = os.stat(item)
            #rate = float(statinfo.st_size)/(width*height)
            #os.rename(item,'++%000.4f+%s'%(rate,item))
            continue
    if width>=1920 and height>=1080:
        os.rename(item,'--%dx%d--%s'%(width,height,item))
    else:
        os.rename(item,'----%dx%d--%s'%(width,height,item))
