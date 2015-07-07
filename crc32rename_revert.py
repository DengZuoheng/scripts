#!/usr/bin/env python
# -*- coding: utf-8 -*-
import binascii
import os,sys
import re
import json

with open('log','r') as log_file:
    file_name_log = json.load(log_file)
    for item in file_name_log:
        for key in item:
            old_name = key
            new_name = item[key]
            os.rename(new_name,old_name)
