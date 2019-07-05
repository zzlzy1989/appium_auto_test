#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: 111
# Author: 简
# Time: 2019/6/26

from appium import webdriver

# 操作系统、系统版本、app应用
desired_caps = {}
desired_caps["automationName"] = "UiAutomator2"
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "5.1"
desired_caps["deviceName"] = "Android Emulator"

# app应用：包名 - 唯一标识
# 如何得到app的包名吗？ apk包。  aapt命令
# aapt dump badging apk应用名
desired_caps["appPackage"]="com.lemon.lemonban"
desired_caps["appActivity"] = "com.lemon.lemonban.activity.WelcomeActivity"

# 2、 appium在线
# 与appium 建立连接，并告诉它，我要干什么！！
webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

# 3、设备在线：连接上USB,开启手机上的USB调试模式。  开发者选项 -
# 在电脑上确认能够识别到设备：adb devices
