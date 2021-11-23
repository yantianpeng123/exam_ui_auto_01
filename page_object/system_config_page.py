#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/10/19  下午4:15
# @Author  : yantianpeng
# @Site    : 
# @File    : system_config_page.py
# @Software: PyCharm
'''
from page_locators.system_config_page_locators import SystemConfigLocators
from page_object.base_page import BasePage
class Sys_Config_Page(BasePage):


    def save(self,sysname):
        """
        系统设置保存
        :param content:
        :return:
        """
        self.wait_element_presence_located(SystemConfigLocators.sys_config_input_loc,action="系统配置输入").send_keys(content=sysname);
        self.wait_element_to_be_clicked(SystemConfigLocators.save_btn_loc,action="系统配置保存").click_element();




    def get_success_tip(self):
        return self.wait_element_is_visiable(SystemConfigLocators.is_success_text_loc,action="系统配置判断").get_element_text();