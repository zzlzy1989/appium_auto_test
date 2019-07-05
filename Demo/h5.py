#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time     : 2019/7/5 0005 20:19 
# @Author   : 蓝天下的风  
# @File     : h5.py 
# Project   : appium_auto_test
# @Software : PyCharm

from appium import webdriver


# 1、识别 app内 的html页面  class: android.webkit.WebView

# web自动化当中，嵌入的html  iframe

# 2、切换 - windows 窗口

# context - 混合应用  NATIVE_APP

# 1、获取所有的context。

# 2、根据context的名字，切换到webview。

# 3、已经切换到html，那后续就是web自动化操作。