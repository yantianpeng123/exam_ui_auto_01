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
from testdata.dept_manage_datas import success_datas,success_no_datas,add_dept_datas,fail_add_dept_datas,edit_dept_datas
from page_object.home_page import HomePage
from page_object.Dept_Manage_Page import Dept_Manage_Page
from common.test_data_handler import replace_args
import allure
import pytest

class TestDeptManage(BaseCase):

    name = "部门管理";

    @allure.title("")
    @pytest.mark.parametrize("data",add_dept_datas)
    def aatest_add_dept(self,Login,data):
        allure.dynamic.title(data["title"]);
        self.driver=Login;
        # 点击系统配置
        hp = HomePage(driver=self.driver);
        dmp = Dept_Manage_Page(driver=self.driver);
        hp.system_config_menu_click();
        # 部门管理
        hp.dept_manage_submenu_click();
        # 生成不重复的部门
        if "#deptname#" in data["request_data"]["deptname"]:
                sql = "select * from sys_depart where dept_name='{}' ;"
                deptname = self.get_no_deptname(sql_templeta=sql);
                self.log.info("在{}功能，生成的用户名是{}".format(data["title"], deptname))
                data["request_data"]["deptname"] = replace_args(data["request_data"]["deptname"], deptname=deptname);
        dmp = Dept_Manage_Page(driver=self.driver);
        # 获取没有添加之前的部门数量
        dept_count_sql = "select * from sys_depart ;"
        before_count = self.db.get_count(sql=dept_count_sql);
        self.log.info("{}页面,在添加之前的部门数量是:{}".format(self.name,before_count));
        # 添加部门
        dmp.add_dept(**data["request_data"]);
        # 开始断言:
        try:
            self.log.info("{}页面开始断言".format(self.name))
            self.beidouxing_assert(check_data=data["check_data"],msg="部门添加功能");
            self.log.info("{}页面-->{}功能--断言成功".format(self.name,data["title"]));
        except Exception as e:
            self.log.exception("{}页面断言失败".format(self.name));
            self.log.info("{}页面--{}功能--断言失败原因:{}".format(self.name,data["title"],e));
            raise e;
        # 获取数据库添加部门之后部门数量
        after_count =  self.db.get_count(sql=dept_count_sql);
        self.log.info("{}功能添加部门成功之后的数量是:{}".format(data["title"],after_count));
        if data["IsSql"] =="1":
            try:
                self.log.info("{}页面--{}功能--开始数据库断言".format(self.name, data["title"]));
                assert before_count<after_count;
                self.log.info("{}页面数据库断言通过".format(self.name));
            except Exception as e:
                self.log.warning("{}页面--{}功能--数据库断言未通过".format(self.name,data["title"]));
                self.log.info("断言未通过原因是:{}".format(e));
                raise e;

    @allure.title("")
    @pytest.mark.parametrize("data",fail_add_dept_datas)
    def aatest_no_dept_name_fail(self,Login,data):
        allure.dynamic.title(data["title"]);
        self.driver = Login;
        # 点击系统配置
        hp = HomePage(driver=self.driver);
        dmp = Dept_Manage_Page(driver=self.driver);
        hp.system_config_menu_click();
        # 部门管理
        get_count_sql="select * from sys_depart ;"
        # 获取新增之间的部门数量
        before_count = self.db.get_count(sql=get_count_sql);
        self.log.info("{}功能在新增之前的部门数量是:{}".format(data["title"],before_count))
        hp.dept_manage_submenu_click();
        dmp.add_dept(**data["request_data"]);
        try:
            self.log.info("{}页面开始断言".format(self.name));
            self.beidouxing_assert(check_data=data["check_data"]);
            self.log.info("{}页面断言通过".format(self.name));
        except Exception as e:
            self.log.exception("{}页面断言失败".format(self.name));
            self.log.info("断言失败原因是:{}".format(e));
            raise e;
        finally:
            self.driver.refresh();

        if data["IsSql"]=="1":
            try:
                self.log.info("{}功能开始数据库校验:".format(data["title"]))
                after_count= self.db.get_count(sql=get_count_sql);
                self.assert_equals(before_count,after_count,msg="数据库校验");
                self.log.info("{}功能断言通过".format(data["title"]));
            except Exception as e:
                self.log.exception("{}功能校验数据库未通过".format(data["title"]));
                self.log.info("{}功能数据库校验未通过原因是:{}".format(data["title"],e));
                raise e;





    @allure.title("")
    @pytest.mark.parametrize("data",success_datas)
    def aatest_serach_no_data_dept(self,Login,data):
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
    def aatest_search_data_dept(self,Login,data):
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

    @allure.title("")
    # @pytest.mark.parametrize("data",)
    def test_delete_dept(self,Login,data):
        allure.dynamic.title(data["title"]);
        self.driver=Login;
        dmp = Dept_Manage_Page(driver=self.driver);  # 输入部门名称
        dmp.delete_dept(**data["request_data"]);
        pass

    @allure.title("")
    @pytest.mark.parametrize("data",edit_dept_datas)
    def test_edit_dept(self,Login,data):
        allure.dynamic.title(data["title"])
        self.driver = Login;
        # 点击系统配置
        hp = HomePage(driver=self.driver);
        hp.system_config_menu_click();
        hp.dept_manage_submenu_click();

        #先进行查询
        dmp = Dept_Manage_Page(driver=self.driver);  # 输入部门名称
        dmp.search_dept(deptname="d_");

        # 点击部门管理
        if "#deptname#" in data["request_data"]["deptname"]:
            # 生成不存在部门
            sql = "select * from sys_depart where dept_name='{}' ;"
            deptname = self.get_no_deptname(sql_templeta=sql);
            self.log.info("在{}页面，生成的用户名是{}".format(self.name, deptname))
            data["request_data"]["deptname"] = replace_args(data["request_data"]["deptname"], deptname=deptname);

        dmp.edit_dept(**data["request_data"]);
        try:
            self.log.info("{}功能开始断言".format(data["title"]));
            self.beidouxing_assert(check_data=data["check_data"]);
            self.log.info("{}功能断言通过".format(data["title"]));
        except Exception as e:
            self.log.exception("{}功能断言未通过".format(data["title"]));
            self.log.info("断言未通过原因是:{}".format(e));
            raise e;
        finally:
            self.driver.refresh();
        if data["IsSql"]=="1":
            self.log.info("{}功能开始数据库断言".format(data["title"]));
            dept_sql = "select * from sys_depart where dept_name='{}' ;".format(deptname)
            # 查询修改成功之后部门数量
            self.log.info("{}功能执行的sql是:{}".format(data["title"],dept_sql));
            after_count = self.db.get_count(sql=dept_sql);
            try:
                self.assert_equals(1,after_count);
            except Exception as e:
                self.log.exception("{}功能数据库断言未通过".format(data["title"]));
                self.log.info("{}功能数据库未通过原因是:{}".format(data["title"]),e);
                raise e;




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




    def get_add_tip(self):
        """部门添加成功"""
        dmp = Dept_Manage_Page(driver=self.driver);
        return dmp.get_add_tip().get_element_text().strip();


    def get_no_deptname_tip(self):
        dmp = Dept_Manage_Page(driver=self.driver);
        return dmp.get_no_deptname_tip().get_element_text();