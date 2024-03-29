#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time     : 2019/6/27 0027 23:07 
# @Author   : 蓝天下的风  
# @File     : app_test1.py
# Project   : appium_auto_test
# @Software : PyCharm

from appium import webdriver

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

# 3、设备在线:连接上USB，开启手机上面的USB调试模式。开发者选项
# 在电脑上确认能够识别的设备：adb devices


# id
driver.find_element_by_id("")
driver.find_elements_by_id("")

# xpath
driver.find_element_by_xpath("")

# class
driver.find_element_by_class_name("")

# content-desc
driver.find_element_by_accessibility_id("")

# uiautomator
uiselector_loc = 'new UiSelector().resourceId("com.miui.home:id/icon_icon").description("音乐")'
driver.find_element_by_android_uiautomator(uiselector_loc)
