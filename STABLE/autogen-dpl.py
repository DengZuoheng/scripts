#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys
import re
import random
filename_list = os.listdir(os.getcwd()) 
music = []
for item in filename_list:
    path = os.path.join(os.getcwd(),item)
    if os.path.isdir(path):
        continue
    r = re.findall(r'\.(dpl|txt|py)$',item)
    if(len(r)>0):
        continue
    music.append(item)

playlist_file = open('0-playlist.dpl','w')
playlist_file.write('DAUMPLAYLIST\n')
begin = random.randint(0,len(music))
playlist_file.write('playname=%s\n'%os.path.join(os.getcwd(),music[begin]))
playlist_file.write('%d\n'%begin)
playlist_file.write('topindex=0\n')
i = 1
for item in music:
    playlist_file.write('%d*file*%s\n'%(i,item))
    playlist_file.write('%d*played*0\n'%i)
    i = i+1
    


