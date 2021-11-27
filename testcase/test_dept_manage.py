#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/11/24  下午11:28
# @Author  : yantianpeng
# @Site    : 
# @File    : test_dept_manage.py
# @Software: PyCharm
'''
from common.base_case_test import BaseCase
from testdata.dept_manage_datas import success_datas
from page_object.home_page import HomePage
from page_object.Dept_Manage_Page import Dept_Manage_Page
from common.test_data_handler import replace_args
import allure
import pytest

class TestDeptManage(BaseCase):

    name = "部门管理";

    @allure.title("")
    @pytest.mark.parametrize("data",success_datas)
    def test_add_dept(self,Login,data):
        allure.dynamic.title(data["title"]);
        self.driver= Login;
        #点击系统配置
        hp = HomePage(driver=self.driver);
        dmp =Dept_Manage_Page(driver=self.driver);
        hp.system_config_menu_click();
        # 部门管理
        hp.dept_manage_submenu_click();

        if "#deptname#" in data["request_data"]["deptname"]:
            sql="select * from sys_depart where dept_name='{}' ;"
            deptname= self.get_no_deptname(sql_templeta=sql);
            self.log.info("在{}页面，生成的用户名是{}".format(self.name, deptname))
            data["request_data"]["deptname"] = replace_args(data["request_data"]["deptname"],deptname=deptname);
        # 输入部门名称
        dmp.search_dept(**data["request_data"]);



        pass;

    @allure.title("")
    @pytest.mark.parametrize("data",)
    def test_delete_dept(self,Login,data):
        allure.dynamic.title(data["title"]);
        pass

    @allure.title("")
    @pytest.mark.parametrize("data")
    def test_edit_dept(self,Login,data):
        allure.dynamic.title(data["title"])
        pass;
