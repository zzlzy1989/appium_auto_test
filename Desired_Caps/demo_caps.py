#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time     : 2019/7/8 0008 21:21 
# @Author   : 蓝天下的风  
# @File     : demo_caps.py 
# Project   : appium_auto_test
# @Software : PyCharm


import yaml

fs = open("caps.yaml",encoding="utf-8")

datas = yaml.load(fs,Loader=yaml.BaseLoader)

print(datas)
