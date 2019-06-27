#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time     : 2019/6/27 0027 23:07 
# @Author   : 蓝天下的风  
# @File     : app_test1.py
# Project   : appium_auto_test
# @Software : PyCharm


# 操作系统、系统版本、app应用
desired_caps = {}
desired_caps["platformName"]="Android"
desired_caps["platformVersion"]="8.1"
desired_caps["deviceName"]="Android Emulator"


# app应用：包名---唯一标识
# 如何得到app的包名？ apk包





# 获取应用包名和入口activity
# 使用命令  aapt dump badging apk应用名