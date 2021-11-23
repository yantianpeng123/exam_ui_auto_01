#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/10/17  下午10:05
# @Author  : yantianpeng
# @Site    : 
# @File    : stu_reg_page_locators.py
# @Software: PyCharm
'''
from selenium.webdriver.common.by import By
class StuRegLocator(object):

    """
    注册页面元素定位
    """
    username_input_loc = (By.XPATH,"//input[@name='userName']");
    realname_input_loc =(By.XPATH,"//input[@name='realName']");
    password_input_loc= (By.XPATH,"//input[@name='password']");
    reg_btn_loc = (By.XPATH,"//span[text()='注册']");
    login_btn_loc = (By.XPATH,"//span[text()='去登录']");

    #错误信息提示页面元素定位
    error_tip_loc = (By.XPATH,"//div[@class='el-form-item__error']");
    # 错误弹出框元素定位
    error_alter_loc =(By.XPATH,"//p[@class='el-message__content']");