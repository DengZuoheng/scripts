#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
config={
    "server":"116.251.211.240",
    "server_port":"8999",
    "local_port":"8118",
    "password":"d2e9n9g7",
    "timeout":600,
    "method":"aes-256-cfb",
}
f=open("/etc/shadowsocks.json","w")
f.write(json.dumps(config))
os.system("nohup /usr/local/bin/ss-local -c /etc/shadowsocks.json &)