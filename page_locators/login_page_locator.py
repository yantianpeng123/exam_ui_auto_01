#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/10/17  上午9:59
# @Author  : yantianpeng
# @Site    : 
# @File    : login_page_locator.py
# @Software: PyCharm
'''
from selenium.webdriver.common.by import By
class LoginPageLocator(object):
    """
    登录页面元素定位
    """

    username_input_locator = (By.XPATH,"//input[@name='username']");
    password_input_locator = (By.XPATH,"//input[@name='password']");
    login_btn_locator = (By.XPATH,"//span[text()='登录']");
    stu_reg_btn_locator = (By.XPATH,"//span[text()='学员注册']");

    #错误信息提示框
    # error_username_notexist_loc= (By.XPATH,"//p[contains(text(),'管理员账号不存在！')]");
    # error_pwd_loc = (By.XPATH,"//p[contains(text(),'账号或密码错误！')]");
    # error_pwd_len_loc=(By.XPATH,"")

    # 账号错误，密码错误 账号不存在错误提示信息
    error_username_pwd_loc =(By.XPATH,'//p[@class="el-message__content"]');
    #密码长度不够提示信息
    error_pwd_len_not_enough_loc=(By.XPATH,"//div[@class='el-form-item__error']")

