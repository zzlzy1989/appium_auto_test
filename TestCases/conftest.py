#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time     : 2019/7/8 0008 20:56 
# @Author   : 蓝天下的风  
# @File     : conftest.py 
# Project   : appium_auto_test
# @Software : PyCharm


import pytest
from Common import dir_config


@pytest.fixture
def login_App():
    # 启动会话
    # 判断登录状态并根据状态做不同的处理

    pass


def base_driver():
    # 固定启动参数 -- 字典
    # 读取yaml的数据文件

    pass