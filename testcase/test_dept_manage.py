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
        # 断言:
        try:
            self.log.info("{}页面开始断言".format(self.name));
            if self.get_dept_name() is None:
                self.beidouxing_assert(check_data=data["check_data"]);
            else:
                for i in self.get_dept_name():
                    assert data["request_data"]["deptname"] in i;
        except Exception as e:
            self.log.exception("{}页面断言未通过".format(self.name));
            self.log.info("{}-->页面断言未通过愿原因".format(e));
            raise e;



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




    def get_dept_name(self):
        dept_names = [];
        dmp = Dept_Manage_Page(driver=self.driver);
        for i in dmp.get_dept_name_tables():
            dept_names.append(i.text);
        return dept_names;

    def get_no_dept_name(self):
        dmp = Dept_Manage_Page(driver=self.driver);
        return dmp.get_no_dept_data().get_element_text();