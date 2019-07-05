#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: app_toast获取
# Author: 简
# Time: 2019/4/1

#toast前提条件


from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction

'''
配置toast请注意：
1、desired_caps["automationName"] = "UiAutomator2"
2、要求安装jdk1.8 64位及以上。配置其环境变量JAVA_HOME和path
3、Android系统5.0以上
4、appium server版本 1.6.3以上

5、xpath表达查找toast
6、只能等待toast存在，而不能等待可见。
'''

#启动参数
desired_caps = {}
desired_caps["automationName"] = "UiAutomator2"
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "8.1"
desired_caps["deviceName"] = "Android Emulator"
desired_caps["noReset"] = True

#保证终端设备上，已安装了对应的app。
desired_caps["appPackage"] = "com.lemon.lemonban"
desired_caps["appActivity"] = "com.lemon.lemonban.activity.WelcomeActivity"


#连接appium server，然后告诉它server，我要干什么。
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

#点击我的柠檬  -- 等待元素可见？？
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,"com.lemon.lemonban:id/navigation_my")))
driver.find_element_by_id("com.lemon.lemonban:id/navigation_my").click()

#点 击我的头像
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,"com.lemon.lemonban:id/fragment_my_lemon_avatar_layout")))
driver.find_element_by_id("com.lemon.lemonban:id/fragment_my_lemon_avatar_layout").click()
#点击登陆按钮
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,"com.lemon.lemonban:id/btn_login")))
driver.find_element_by_id("com.lemon.lemonban:id/btn_login").click()

#获取 toast信息
#toast xpath表达式
toast_loc = '//*[contains(@text,"手机号码或密码")]'
#不能用等待元素可见。只能用等待元素存在。
try:
    WebDriverWait(driver,10,0.01).until(EC.presence_of_all_elements_located((MobileBy.XPATH,toast_loc)))
    print(driver.find_element_by_xpath(toast_loc).text)
except:
    print("没有获取 到toast信息！")