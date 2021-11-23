#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/10/17  上午11:02
# @Author  : yantianpeng
# @Site    : 
# @File    : login_page.py
# @Software: PyCharm
'''
from page_object.base_page import BasePage
from page_locators.login_page_locator import LoginPageLocator
class Login_Page(BasePage):


    name = "登录页面"
    def login(self,username,password):
        """
        登录功能
        :param username:
        :param password:
        :return:
        """
        self.wait_time(time=5); # 休息五秒钟等待页面获取元素
        #输入账号
        self.wait_element_is_visiable(locator=LoginPageLocator.username_input_locator,action="登录").send_keys(content=username);
        #输入密码
        self.wait_element_is_visiable(locator=LoginPageLocator.password_input_locator,action="登录").send_keys(content=password);
        #点击登录按钮
        self.wait_element_is_visiable(locator=LoginPageLocator.login_btn_locator,action="登录").click_element();


    def stu_reg(self):
        """
        学员注册按钮
        :return:
        """
        self.wait_element_is_visiable(locator=LoginPageLocator.stu_reg_btn_locator,action="点击学员注册按钮").click_element();


    def  get_error_username_pwd_tip(self):
        """
        获取密码或者账号错误提示信息
        :return:
        """
        error_input_text= self.wait_element_presence_located(locator=LoginPageLocator.error_username_pwd_loc,action="获取登录错误提示信息").get_element_text();
        return error_input_text;

    def get_error_pwd_not_enough(self):
        """
        获取密码长度不足错误提示信息
        :return:
        """
        error_pwd_text = self.wait_element_presence_located(locator=LoginPageLocator.error_pwd_len_not_enough_loc,action="获取密码长度不足提示信息").get_element_text();
        return error_pwd_text;