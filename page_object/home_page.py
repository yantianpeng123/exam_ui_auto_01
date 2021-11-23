#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/10/17  下午2:04
# @Author  : yantianpeng
# @Site    : 
# @File    : home_page.py
# @Software: PyCharm
'''
from page_object.base_page import BasePage
from page_locators.home_page_locators import HomePageLocator
from time import sleep
class HomePage(BasePage):

    name = "首页";

    def welcome_isexist(self):
        return self.wait_element_is_visiable(locator=HomePageLocator.wel_text_loc,action="首页").get_element();




    def system_config_menu_click(self):

        #点击系统设置
        self.wait_element_presence_located(HomePageLocator.system_config_menu_loc,action="点击系统设置").click_element();
        self.wait_time(2);


    def system_config_submenu_click(self):
        if "sys/config" not in self.driver.current_url:
            # 点击系统配置
            self.wait_element_presence_located(HomePageLocator.system_config_submenu_loc,action="点击系统配置").click_element();

    def user_manage_submenu_click(self):
        if "sys/user" not in self.driver.current_url:
            self.wait_element_presence_located(HomePageLocator.users_manage_submenu_loc,action="点击系统配置").click_element();

    def login_out(self):
        self.wait_element_is_visiable(locator=HomePageLocator.index_icon_loc,action="首页退出").click_element();
        sleep(0.5);
        self.wait_element_presence_located(locator=HomePageLocator.login_out_loc,action="首页退出").click_element();
