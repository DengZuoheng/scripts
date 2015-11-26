import os
import sys

def insert_line(filepath,line_num,new_text):
    f = open(filepath, 'r')
    s = f.read()
    f.close()
    l = s.splitlines()
    l.insert(line_num, new_text)
    s = '\n'.join(l)
    f = open(filepath, 'w')
    f.write(s)
    f.close()

def change_line(filepath,line_num,new_text):
    f = open(filepath, 'r')
    s = f.read()
    f.close()
    l = s.splitlines()
    l[line_num]=new_text
    s = '\n'.join(l)
    f = open(filepath, 'w')
    f.write(s)
    f.close()

if __name__=='__main__':
    os.system('rm -r -f apue.2e')
    os.system('rm -r -f apue.2e.tar')
    os.system('wget -y p://www.apuebook.com/src.2e.tar.gz')
    os.system('gzip -d *.gz ')
    os.system('tar xvf *.tar ')
    os.chdir('apue.2e')
    change_line('Make.defines.linux',6,'WKDIR=%s'%os.getcwd())
    insert_line('include/apue.h',17,'#define ARG_MAX 4096\\n')
    insert_line('threadctl/getenv1.c',0,'#include "apue.h"')
    insert_line('threadctl/getenv3.c',0,'#include "apue.h"')
    change_line('threads/badexit2.c',31,
        'printf("thread 2: ID is %d\\n", (int)pthread_self());\n')
    change_line('ipp/ipp.h',122,'#define Status u.st')
    change_line('ipp/printd.c',977,'i = ntohs(hp->Status);')

