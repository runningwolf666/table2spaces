#!/usr/bin/env python3
#-*- coding:utf-8 -*-
请在Python3下运行此程序='Please run this program with Python3'
'''table to space'''
import sys

TAB_SIZE = 4

filenames = sys.argv[1:]
for filename in filenames:
    if filename.endswith('py'):
        with open(filename, 'r', encoding='utf-8') as f:
            allcontent = f.read()

        allcontent = allcontent.replace('\t', ' '*TAB_SIZE)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(allcontent)
