#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
ip = '116.251.218.79'
port = '8999'
pw = 'd2e9n9g7'
method = 'aes-256-cfb'
cmd = "nohup /usr/local/bin/ss-server -s %s -p %s -k %s -m %s >&1 &"%(ip,port,pw,method)
os.system(cmd)