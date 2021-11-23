#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/10/19  下午4:21
# @Author  : yantianpeng
# @Site    : 
# @File    : test_sys_config.py
# @Software: PyCharm
'''
from common.base_case_test import BaseCase
from testdata.sys_config_datas import sys_config_data

from page_object.system_config_page import Sys_Config_Page
from page_object.home_page import HomePage
import pytest
import allure
class TestSysConfig(BaseCase):
    name = "系统配置页面";


    @pytest.mark.parametrize("data",sys_config_data)
    @allure.title("")
    def test_success(self,Login,data):
        allure.dynamic.title(data["title"]);
        self.driver =Login;
        # 登录
        # 点击系统设置
        hp =HomePage(driver=self.driver);
        hp.system_config_menu_click();
        hp.system_config_submenu_click();
        sc = Sys_Config_Page(driver=self.driver);

        # 输入
        sc.save(**data["request_data"]);
        # 断言
        self.beidouxing_assert(check_data=data["check_data"]);




    def get_success_tip(self):
        sc = Sys_Config_Page(driver=self.driver);
        return sc.get_success_tip();
