#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import urllib2
import sys
import re
def update_config(remarks,config,config_path):
    config_fp = open(config_path,'r')
    gui_config = json.load(config_fp)
    config_fp.close()
    index = 0
    for item in gui_config['configs']:
        index += 1
        if item.get('remarks') == remarks:
            item.update(config)
            break
    gui_config['index']=index-1
    config_fp = open(config_path,'w')
    json.dump(gui_config,config_fp,indent=4)
    config_fp.close()

def get_new_config():
    ISS_URL = 'http://www.ishadowsocks.com'
    result = urllib2.urlopen(ISS_URL)
    server_pt = r'<h4>C服务器地址\s*:\s*(?P<server>\S+?)\s*</h4>'
    port_pt = r'<h4>端口:(?P<server_port>\d+)\s*</h4>'
    password_pt = r'<h4>C密码\s*:\s*(?P<password>\S+?)\s*</h4>'
    method_pt = r'<h4>加密方式\s*:\s*(?P<method>\S+)\s*</h4>'
    pattern = r'\s*'.join([server_pt,port_pt,password_pt,method_pt])
    result_str = result.read()
    ret = re.search(pattern.decode('utf-8'),result_str.decode('utf-8') )
    if ret:
        di = map(lambda item: (item,ret.group(item)),
            ['server','server_port','password','method'])
        return dict(di)

if __name__=='__main__':
    config = get_new_config()
    config_path = sys.argv[1]
    update_config('iShadowsocks',config,config_path)
    
