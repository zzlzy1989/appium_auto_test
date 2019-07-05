#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: app_startActivity
# Author: 简
# Time: 2019/4/1
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
#跨应用
#应用当中可以切换到其它的acitivity
#启动参数
desired_caps = {}
desired_caps["automationName"] = "UiAutomator2"
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "7.1"
desired_caps["deviceName"] = "Android Emulator"
desired_caps["noReset"] = True

#保证终端设备上，已安装了对应的app。
desired_caps["appPackage"] = "com.lemon.lemonban"
desired_caps["appActivity"] = "com.lemon.lemonban.activity.WelcomeActivity"


#连接appium server，然后告诉它server，我要干什么。
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,"com.lemon.lemonban:id/navigation_my")))


#直接进入登陆操作页面:自己的包名。
driver.start_activity("com.lemon.lemonban","com.lemon.lemonban.activity.LoginActActivity")

import time
time.sleep(3)

#去打开另外一个前程贷app:app的包名。activity只能是入口activity
driver.start_activity("com.xxzb.fenwoo","com.xxzb.fenwoo.activity.addition.WelcomeActivity")