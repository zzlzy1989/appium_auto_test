#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time     : 2019/6/25 0025 22:49 
# @Author   : 蓝天下的风  
# @File     : dir_config.py 
# Project   : appium_auto_test
# @Software : PyCharm



import os
#框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
# 测试数据
testdatas_dir =  os.path.join(base_dir,"TestDatas")
# 测试用例
testcases_dir =  os.path.join(base_dir,"TestCases")
# 测试报告-HTML
htmlreport_dir =  os.path.join(base_dir,"Outputs/reports")
# 日志存放地址
logs_dir =  os.path.join(base_dir,"Outputs/logs")
# 配置文件地址
config_dir =  os.path.join(base_dir,"Config")

screenshot_dir = os.path.join(base_dir,"Outputs/screenshots")

# APP启动参数配置路径
caps_dir = os.path.join(base_dir,"Desired_Caps")

print(screenshot_dir)