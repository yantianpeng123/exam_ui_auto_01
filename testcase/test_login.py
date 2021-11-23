#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/10/17  上午11:13
# @Author  : yantianpeng
# @Site    : 
# @File    : test_login.py
# @Software: PyCharm
'''
from common.base_case_test import BaseCase
from testdata.login_datas import success_data,fail_data,fail_data_pwd_notlen
from page_object.login_page import Login_Page
from page_object.home_page import HomePage;
import pytest
class Test_Login(BaseCase):

    name = "登录功能"

    @pytest.mark.parametrize("data", fail_data)
    def test_login_fail(self, driver, data):
        self.driver = driver;
        lp = Login_Page(driver=self.driver);
        lp.login(**data["request_data"]);
        self.login_assert(check_data=data["check_data"]);

    @pytest.mark.parametrize("data",fail_data_pwd_notlen)
    def test_login_fail_pwd_notlen(self,driver,data):
        self.driver=driver;
        self.driver.refresh();
        lp= Login_Page(driver=self.driver);
        lp.login(**data["request_data"]);
        self.login_assert(check_data=data["check_data"])

    @pytest.mark.parametrize("data",success_data)
    def test_login_success(self,driver,data):
        self.driver =driver;
        self.driver.refresh();
        lp = Login_Page(driver=self.driver);
        lp.login(**data["request_data"]);
        self.login_assert(check_data=data["check_data"]);


    def login_assert(self, check_data):
        """
        自定义登录断言
        :param check_data:
        :return:
        """
        method = getattr(self, check_data['method']);
        assert method() == check_data['value'];


    def get_error_username_pwd_tip(self):
        error_tip = Login_Page(driver=self.driver).get_error_username_pwd_tip()
        return error_tip.strip();

    def get_error_pwd_not_enough(self):
        error_tip = Login_Page(driver=self.driver).get_error_pwd_not_enough();
        return error_tip.strip();



    def is_login(self):
        """
        判断是否等成功
        :return:
        """
        try:
            HomePage(driver=self.driver).welcome_isexist();
            return True;
        except Exception as e:
            return False;

