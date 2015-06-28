
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import binascii
import os,sys
import re
import random
import json
 
def CRC32_from_file(filename):
    buf = open(filename,'rb').read()
    buf = (binascii.crc32(buf) & 0xFFFFFFFF)
    return "%08X" % buf

def is_pic(extension):
    return extension.lower() in ['jpg','png','jpeg','gif','tif','bmp']

filename_list = os.listdir(os.getcwd()) 
music = []
log = []
for item in filename_list:
    old_name = item
    path = os.path.join(os.getcwd(),item)
    if os.path.isdir(path):
        continue
    extension = os.path.splitext(item)[1][1:]
    if False == is_pic(extension):
        continue
    crc32 = CRC32_from_file(item)
    try:
        new_name = ''.join([crc32,'.',extension])
        os.rename(item, new_name)
        log_str = '%s >>> %s'%(old_name,new_name)
        log.append(log_str)
        print(log_str)
    except:
        log_str = '%s didn\'t rename'%old_name
        log.append(log_str)
        print(log_str)
        
with open('log', 'w') as outfile:
    json.dump(log, outfile)