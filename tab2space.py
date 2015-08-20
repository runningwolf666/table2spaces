#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import sys

TAB_SIZE = 4

filenames = sys.argv[1:]
for filename in filenames:
    with open(filename, 'r', encoding='utf-8') as f:
        # print(help(f))
        allcontent = f.readlines()
    
    allcontent2 = []
    for item in allcontent:
        allcontent2.append(item.replace('\t', ' '*TAB_SIZE))

    with open('new_'+filename, 'w', encoding='utf-8') as f:
        f.writelines(allcontent2)
