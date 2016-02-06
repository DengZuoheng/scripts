#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import urllib,urllib2

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class console(object):
    @classmethod
    def fail(cls, str):
        print bcolors.FAIL + str.encode('gbk','ignore') + bcolors.ENDC

    @classmethod
    def log(cls, str):
        print str.encode('gbk','ignore')

    @classmethod
    def info(cls, str):
        print bcolors.OKBLUE + str.encode('gbk','ignore') + bcolors.ENDC

def echo(obj):
    errorCode = obj.get('errorCode')
    if errorCode == 0:
        if 'translation' in obj:
            console.info(u'有道翻译: ')
            console.log(','.join(obj['translation']))
        if 'basic' in obj:
            console.info(u'基本词典:')
            console.log('\n'.join(obj['basic'].get('explains')))
        if 'web' in obj:
            console.info(u'网络释义:')
            for item in obj['web']:
                console.log(u'%s: %s'%(item['key'],'; '.join(item['value'])))
        console.log('')

    elif errorCode == 20:
        console.fail(u'要翻译的文本过长')
    elif errorCode == 30:
        console.fail(u'无法进行有效的翻译')
    elif errorCode == 40:
        console.fail(u'不支持的语言类型')
    elif errorCode == 50:
        console.fail(u'无效的key')
    elif errorCode == 60:
        console.fail(u'无词典结果，仅在获取词典结果生效')
    else:
        console.fail(u'反正出错了, 怎么错的不知道')

def fanyi(q):
    url_args = {
        'keyfrom':'libeicsu',
        'key':'845720444',
        'type':'data',
        'doctype':'json',
        'version':'1.1',
        'q':q.encode('UTF-8')
    }
    encoded_args = urllib.urlencode(url_args)
    base_url = 'http://fanyi.youdao.com/openapi.do'
    url = '?'.join([base_url,encoded_args])
    result = urllib2.urlopen(url)
    result = result.read()
    j = json.loads(result)
    echo(j)
    

if __name__=='__main__':
    argv = sys.argv
    if len(argv) > 1:
        args = argv[1:]
        args = [q.decode('gbk','ignore') for q in args]
        q = u' '.join(args)
        fanyi(q)
