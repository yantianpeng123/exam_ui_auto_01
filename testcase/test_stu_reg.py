#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/10/17  下午10:25
# @Author  : yantianpeng
# @Site    : 
# @File    : test_stu_reg.py
# @Software: PyCharm
'''
from common.base_case_test import BaseCase
from testdata.stu_reg_datas import success_data,fail_data_userexist,fail_data_user_error,fail_data_realname_error,fail_data_pwd_error
from page_object.stu_reg_page import Stu_Reg_Page
from common.test_data_handler import replace_args
from page_object.login_page import Login_Page
from page_object.home_page import HomePage
import pytest
import allure
@pytest.mark.usefixtures("driver")
class Test_Stu_Reg(BaseCase):
    name = "注册页面";





    @pytest.mark.parametrize("data",success_data)
    def test_success(self,data,driver):
        """
        测试成功
        :param data:
        :param driver:
        :return:
        """
        self.driver= driver;
        sr = Stu_Reg_Page(driver=self.driver);
        lp = Login_Page(driver=self.driver)
        hp= HomePage(driver=self.driver);
        #得到不存在的用户名
        sql="select * from sys_user where user_name ='{}'";
        username = self.get_no_username(sql_templeta=sql);
        self.log.info("在{}页面，生成的用户名是{}".format(self.name,username));
        #用户名称替换
        if "#username#" in data["request_data"]["username"]:
            data["request_data"]["username"]=replace_args(data["request_data"]["username"],username=username);

        # 替换真实姓名(和用户名保持一致)
        if "#realname#" in data["request_data"]["realname"]:
            data["request_data"]["realname"] = replace_args(data["request_data"]["realname"], realname=username);

        # 页面跳转
        lp.stu_reg();
        sr.stu_reg_btn_click(**data["request_data"]);
        #断言:
        self.beidouxing_assert(check_data=data["check_data"])
        # 退出登录
        hp.login_out();


    @pytest.mark.parametrize("data",fail_data_userexist)
    def test_fail_userexist(self,driver,data):
        self.driver = driver;
        sr = Stu_Reg_Page(driver=self.driver);
        lp = Login_Page(driver=self.driver)
        #得到已经存在的用户名
        sql = "select * from sys_user limit 1";
        users = self.db.get_one_data(sql=sql);
        username = users["user_name"];
         #用户名称替换
        if "#username#" in data["request_data"]["username"]:
            data["request_data"]["username"]=replace_args(data["request_data"]["username"],username=username);

        #替换真实姓名
        if "#realname#" in data["request_data"]["realname"]:
            data["request_data"]["realname"] = replace_args(data["request_data"]["realname"],realname=username);
        # 页面跳转
        lp.stu_reg();
        sr.stu_reg_btn_click(**data["request_data"]);
        #断言
        self.beidouxing_assert(check_data=data["check_data"]);

    @allure.title("")
    @pytest.mark.parametrize("data", fail_data_user_error)
    def test_fail_user_error(self, driver, data):
        allure.dynamic.title(data["title"]);
        self.driver=driver;
        self.driver.refresh();
        sr = Stu_Reg_Page(driver=self.driver);
        #学员注册
        sr.stu_reg_btn_click(**data["request_data"]);
        self.beidouxing_assert(check_data=data["check_data"]);


    @allure.title("")
    @pytest.mark.parametrize("data",fail_data_realname_error)
    def test_fail_error_realname(self,driver,data):
        allure.dynamic.title(data['title']);
        self.driver = driver;
        self.driver.refresh();# 刷新页面
        sr = Stu_Reg_Page(driver=self.driver);
        sr.stu_reg_btn_click(**data["request_data"]);
        self.beidouxing_assert(check_data=data["check_data"]);


    @allure.title("")
    @pytest.mark.parametrize("data",fail_data_pwd_error)
    def test_fail_error_pwd(self,driver,data):
        allure.dynamic.title(data["title"]);
        self.driver=driver;
        self.driver.refresh();
        sr= Stu_Reg_Page(driver=self.driver);
        sr.stu_reg_btn_click(**data["request_data"]);
        self.beidouxing_assert(check_data=data["check_data"]);

    def is_login(self):
        """
        判断是否登录
        :return:
        """
        hp = HomePage(driver=self.driver);
        try:
            hp.welcome_isexist();
            return True;
        except :
            return False

    def get_error_alter_tip(self):
        """
        获取错误弹框提示
        :return:
        """
        sr = Stu_Reg_Page(driver=self.driver);
        return sr.get_error_alter_tip();



    def get_error_tip(self):
        sr = Stu_Reg_Page(driver=self.driver);
        return sr.get_error_tip()
