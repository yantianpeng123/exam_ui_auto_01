#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/10/19  下午4:08
# @Author  : yantianpeng
# @Site    : 
# @File    : system_config_page_locators.py
# @Software: PyCharm
'''
from selenium.webdriver.common.by import By

class SystemConfigLocators(object):

    #系统显示名称
    sys_config_input_loc = (By.XPATH,'//input[@placeholder="系统显示名称"]');

    # 保存按钮
    save_btn_loc=(By.XPATH,'//button[@type="button"]//span[text()="保存"]');

    #保存成功配置
    is_success_text_loc = (By.XPATH,'//h2[@class="el-notification__title"]');
