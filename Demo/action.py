#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time     : 2019/7/1 0001 21:33 
# @Author   : 蓝天下的风  
# @File     : action.py 
# Project   : appium_auto_test
# @Software : PyCharm



from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy

# 操作系统、系统版本、app应用
desired_caps = {}

desired_caps["automationName"]="UiAutomator2"
desired_caps["platformName"]="Android"
desired_caps["platformVersion"]="7.1.2"
desired_caps["deviceName"]="Android Emulator"
desired_caps["noReset"]=True

# app应用：包名---唯一标识
# 如何得到app的包名？ apk包
# 获取应用包名和入口activity
# 使用命令  aapt dump badging apk应用名

desired_caps["appPackage"]="com.lemon.lemonban"
desired_caps["appActivity"]="com.lenmon.lemonban.activity.WelcomeActivity"

# 2、与appium建立连接
# 与 appium 建立连接，并告诉他，要干什么？
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

# 等待
loc = (MobileBy.ID,"")
WebDriverWait(driver,30).until(EC.visibility_of_element_located(loc))