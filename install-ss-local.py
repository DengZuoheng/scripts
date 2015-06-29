#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
import re
config={
    "server":"116.251.218.79",
    "server_port":8999,
    "local_port":1080,
    "password":"d2e9n9g7",
    "timeout":600,
    "method":"aes-256-cfb"
}

if __name__=='__main__':
    os.system('apt-get install python-pip')
    os.system('pip install shadowsocks')
    f=open("/etc/ss.conf","w")
    json.dump(config,f)
    f.close()
    f=open("/etc/ss_start.sh","w")
    f.write("nohup sslocal -c /etc/ss.conf >/dev/null &")
    f.close()
    f = open("/etc/rc.local","r")
    s = f.read()
    f.close()
    l = s.splitlines()
    for i in range(len(l)):
        if re.match(r'^\s*?exit 0\s*?$',l[i]):
            l.insert(i,'sudo sh /etc/ss_start.sh')
            break
        if re.match(r'^\s*sudo sh /etc/ss_start.sh\s*$',l[i]):
            break
    s = '\n'.join(l)
    f = open("/etc/rc.local","w")
    f.write(s)
    f.close()
    os.system('nohup sslocal -c /etc/ss.conf >/dev/null &')
