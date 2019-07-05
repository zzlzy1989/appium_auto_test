#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/12/14 11:19

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
desired_caps = {}
desired_caps["automationName"] = "UiAutomator2"
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "5.1"
desired_caps["deviceName"] = "Android Emulator"
desired_caps["appPackage"] = "com.xxzb.fenwoo"
desired_caps["appActivity"] = "com.xxzb.fenwoo.activity.addition.WelcomeActivity"
desired_caps["noReset"] = True
import time
#连接appium server,告诉appium，代码要操作哪个设备上的哪个app
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
#滑屏操作
# window_size = driver.get_window_size()
# for index in range(0,3):
#     driver.swipe(window_size["width"]*0.9,window_size["height"]*0.5,window_size["width"]*0.1,window_size["height"]*0.5)
#     time.sleep(0.5)

#
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.XPATH,'//android.widget.TextView[@text=\"我\"]')))
driver.find_element_by_xpath('//android.widget.TextView[@text=\"我\"]').click()

#
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,'com.xxzb.fenwoo:id/et_phone')))
driver.find_element_by_id('com.xxzb.fenwoo:id/et_phone').send_keys("18684720553")
driver.find_element_by_id('com.xxzb.fenwoo:id/btn_next_step').click()

#
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,'com.xxzb.fenwoo:id/et_pwd')))
driver.find_element_by_id('com.xxzb.fenwoo:id/et_pwd').send_keys("python")
driver.find_element_by_id('com.xxzb.fenwoo:id/btn_next_step').click()

# #手势密码 - 马上设置
# WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,"com.xxzb.fenwoo:id/btn_confirm")))
# driver.find_element_by_id("com.xxzb.fenwoo:id/btn_confirm").click()
#
# #创建手势密码
# WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,"com.xxzb.fenwoo:id/btn_gesturepwd_guide")))
# driver.find_element_by_id("com.xxzb.fenwoo:id/btn_gesturepwd_guide").click()

#安全中心
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,'com.xxzb.fenwoo:id/textView11')))
driver.find_element_by_id("com.xxzb.fenwoo:id/textView11").click()

#手势设置
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,"com.xxzb.fenwoo:id/layout_gesture_password")))
driver.find_element_by_id("com.xxzb.fenwoo:id/layout_gesture_password").click()

#开启手势密码开关
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,"com.xxzb.fenwoo:id/switch_gesture")))
driver.find_element_by_id("com.xxzb.fenwoo:id/switch_gesture").click()

#创建手势密码页面
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,"com.xxzb.fenwoo:id/btn_gesturepwd_guide")))
driver.find_element_by_id("com.xxzb.fenwoo:id/btn_gesturepwd_guide").click()

#手势设置样板页面 ==演示页面
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,"com.xxzb.fenwoo:id/right_btn")))
driver.find_element_by_id("com.xxzb.fenwoo:id/right_btn").click()

#手势设置 页面
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,"com.xxzb.fenwoo:id/gesturepwd_create_lockview")))
ele = driver.find_element_by_id("com.xxzb.fenwoo:id/gesturepwd_create_lockview")

#元素大小
ele_size = ele.size
#起始坐标点
start = ele.location
#步长
step = ele_size["height"]/6
#九宫格的五个坐标点
point1 = (start["x"] + step,start["y"] + step)
point2 = (point1[0] + 2*step,point1[1])
point3 = (point2[0] + 2*step,point2[1])
point4 = (point3[0] - 2*step,point3[1] + 2*step)
point5 = (point4[0],point4[1] + 2*step )

tc = TouchAction(driver)
#步骤：先按住第一个点不松，移动到第五个点，然后释放。
tc.press(x=point1[0],y=point1[1]).wait(200).move_to(x=point2[0],y=point2[1]).\
    wait(200).move_to(x=point3[0],y=point3[1]).wait(200).move_to(x=point4[0],y=point4[1]) \
    .wait(200).move_to(x=point5[0],y=point5[1]).wait(200).release().perform()