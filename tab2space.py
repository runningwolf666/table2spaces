#!/usr/bin/env python3
#-*- coding:utf-8 -*-
请在Python3下运行此程序='Please run this program with Python3'
'''table to space'''
import sys

TAB_SIZE = 4

allcontent, content_tab2space = [], []
filenames = sys.argv[1:]
for filename in filenames:
    with open(filename, 'r', encoding='utf-8') as f:
        # print(help(f))
        allcontent = f.readlines()

for item in allcontent:
    content_tab2space.append(item.replace('\t', ' '*TAB_SIZE))

with open('tab2space_'+filename, 'w', encoding='utf-8') as f:
    f.writelines(content_tab2space)
