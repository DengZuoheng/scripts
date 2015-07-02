#!/usr/bin/env python
# -*- coding: utf-8 -*-
import binascii
import os,sys
import re
import json

f = open('log','r')
file_name_log = json.load(f)
for item in file_name_log:
    for key in item:
        old_name = key
        new_name = item[key]
        os.rename(new_name,old_name)
