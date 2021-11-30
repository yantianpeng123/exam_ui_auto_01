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
from testdata.dept_manage_datas import success_datas,success_no_datas
from page_object.home_page import HomePage
from page_object.Dept_Manage_Page import Dept_Manage_Page
from common.test_data_handler import replace_args
import allure
import pytest

class TestDeptManage(BaseCase):

    name = "部门管理";

    @allure.title("")
    @pytest.mark.parametrize("data",success_datas)
    def test_serach_no_data_dept(self,Login,data):
        allure.dynamic.title(data["title"]);
        self.driver= Login;
        #点击系统配置
        hp = HomePage(driver=self.driver);
        dmp =Dept_Manage_Page(driver=self.driver);
        hp.system_config_menu_click();
        # 部门管理
        hp.dept_manage_submenu_click();
        dmp.search_dept(**data["request_data"]);
        # 断言:
        try:
            self.log.info("{}页面开始断言".format(self.name));
            for i in self.get_dept_name():
                self.log.info("{}当前查询到部门是:{}".format(self.name,i));
                assert data["request_data"]["deptname"] in i;
                self.log.info("{}页面断言通过".format(self.name));
        except Exception as e:
            self.log.exception("{}页面断言未通过".format(self.name));
            self.log.info("{}-->页面断言未通过愿原因".format(e));
            raise e;



    @allure.title("")
    @pytest.mark.parametrize("data",success_no_datas)
    def test_search_data_dept(self,Login,data):
        allure.dynamic.title(data["title"]);
        self.driver=Login;
        if "#deptname#" in data["request_data"]["deptname"]:
            sql="select * from sys_depart where dept_name='{}' ;"
            deptname= self.get_no_deptname(sql_templeta=sql);
            self.log.info("在{}页面，生成的用户名是{}".format(self.name, deptname))
            data["request_data"]["deptname"] = replace_args(data["request_data"]["deptname"],deptname=deptname);

        dmp =Dept_Manage_Page(driver=self.driver);# 输入部门名称
        dmp.search_dept(**data["request_data"]);
        try:
            self.log.info("{}页面开始断言".format(self.name));
            self.beidouxing_assert(check_data=data["check_data"]);
            self.log.info("{}页面断言成功".format(self.name));
        except Exception as e:
            self.log.exception("{}功能断言失败".format(self.name));
            self.log.info("{}页面断言失败原因是:{}".format(self.name,e));
            raise e;
        pass;

    @allure.title("")
    # @pytest.mark.parametrize("data",)
    def test_delete_dept(self,Login,data):
        allure.dynamic.title(data["title"]);
        pass

    @allure.title("")
    # @pytest.mark.parametrize("data")
    def test_edit_dept(self,Login,data):
        allure.dynamic.title(data["title"])
        pass;




    def get_dept_name(self):
        dept_names = [];
        dmp = Dept_Manage_Page(driver=self.driver);
        for i in dmp.get_dept_name_tables():
            dept_names.append(i.text);
        self.log.info("{}页面获取的部门名称是:{}".format(self.name,dept_names));
        return dept_names;

    def get_no_dept_name(self):
        dmp = Dept_Manage_Page(driver=self.driver);
        return dmp.get_no_dept_data().get_element_text();