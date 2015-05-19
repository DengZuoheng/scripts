
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import binascii
import os,sys
import re
import random
 
def CRC32_from_file(filename):
    buf = open(filename,'rb').read()
    buf = (binascii.crc32(buf) & 0xFFFFFFFF)
    return "%08X" % buf


filename_list = os.listdir(os.getcwd()) 
music = []
for item in filename_list:
    old_name = item
    path = os.path.join(os.getcwd(),item)
    if os.path.isdir(path):
        continue
    extension = os.path.splitext(item)[1][1:]
    crc32 = CRC32_from_file(item)
    try:
        new_name = ''.join([crc32,'.',extension])
        os.rename(item, new_name)
        print('%s >>> %s'%(old_name,new_name))
    except:
        print('%s didn\'t rename'%old_name)