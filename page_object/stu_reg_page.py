#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/10/17  下午10:17
# @Author  : yantianpeng
# @Site    : 
# @File    : stu_reg_page.py
# @Software: PyCharm
'''
from page_object.base_page import BasePage
from page_locators.stu_reg_page_locators import StuRegLocator
class Stu_Reg_Page(BasePage):

    def stu_reg_btn_click(self,username,realname,password):
        """
        学生注册
        :param username:
        :param realname:
        :param password:
        :return:
        """
        self.wait_time(time=5)
        self.wait_element_presence_located(locator=StuRegLocator.username_input_loc,action="学员注册").send_keys(content=username);
        self.wait_element_presence_located(locator=StuRegLocator.realname_input_loc,action="学员注册").send_keys(content=realname);
        self.wait_element_presence_located(locator=StuRegLocator.password_input_loc,action="学员注册").send_keys(content=password);
        self.wait_element_to_be_clicked(locator=StuRegLocator.reg_btn_loc,action="学员注册").click_element();


    def go_login_btn(self):
        """
        去登录功能
        :return:
        """
        self.wait_element_to_be_clicked(locator=StuRegLocator.login_btn_loc).click_element();

    def get_error_tip(self):
        """
        获取错误提示信息
        :return:
        """
        return self.wait_element_presence_located(locator=StuRegLocator.error_tip_loc,action="注册页面获取错误提示信息").get_element_text();


    def get_error_alter_tip(self):
        """
        获取弹出框错误提示框
        :return:
        """
        return self.wait_element_presence_located(locator=StuRegLocator.error_alter_loc,action="注册页面获取弹框错误").get_element_text();