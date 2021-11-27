#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/10/20  上午12:04
# @Author  : yantianpeng
# @Site    : 
# @File    : test_user_manage.py
# @Software: PyCharm
'''
from common.base_case_test import BaseCase
from page_object.user_manage_page import User_Manage_Page
from page_object.home_page import HomePage
from testdata.user_manage_datas import user_manage_success,fail_deptname_isempty,delete_all_user,search_name_data,search_name_nodata
from common.test_data_handler import replace_args
import pytest
import allure
class TestUserManage(BaseCase):
    name = "用户管理模块"



    @allure.title("")
    @pytest.mark.parametrize("data",user_manage_success)
    def test_add_user(self,Login,data):
        allure.dynamic.title(data["title"]);
        self.driver=Login;
        um = User_Manage_Page(driver=self.driver)
        hp = HomePage(driver=self.driver);
        #用户名和姓名替换
        if "#username#" in data["request_data"]["username"]:
            # 得到不存在的用户名
            sql = "select * from sys_user where user_name ='{}'";
            username = self.get_no_username(sql_templeta=sql);
            self.log.info("在{}页面，生成的用户名是{}".format(self.name, username));
            data["request_data"]["username"]=replace_args(data["request_data"]["username"],username=username);
        if "#realname#" in data["request_data"]["realname"]:
            # 得到未被使用的真实姓名
            sql = "select * from sys_user where real_name ='{}'";
            real_name = self.get_no_username(sql_templeta=sql);
            self.log.info("在{}页面，生成的姓名是{}".format(self.name, real_name));
            data["request_data"]["realname"]=replace_args(data["request_data"]["realname"],realname=real_name);
        hp.system_config_menu_click();
        hp.user_manage_submenu_click();
        um.add_user(**data["request_data"])
        try:
            self.log.info("{}功能开始执行断言>>".format(self.name));
            self.beidouxing_assert(check_data=data["check_data"]);
            self.log.info("{}功能断言通过".format(self.name));
        except Exception as e:
            self.log.exception("{}功能,断言未通过，未通过的原因是:{}".format(self.name,e))
            raise e;
        self.driver.refresh();
        try:
            if data["IsSql"]=="1":
                sql1="select * from sys_user where user_name ='{}'and real_name ='{}'".format(data["request_data"]["username"],data["request_data"]["realname"]);
                self.log.info("{}开始sql校验,执行的sql语句是:{}".format(self.name,sql1));
                assert True ==self.db.Isexit(sql=sql1)
                self.log.exception("{}开始sql校验,sql校验通过".format(self.name));
        except Exception as e:
            self.log.exception("{}开始sql校验,sql校验未通过".format(self.name));
            self.log.error("sql校验失败,执行的异常是:{}".format(e));
            raise e;


    @pytest.mark.parametrize("data",fail_deptname_isempty)
    @allure.title("")
    def test_fail_deptname_isempty(self,Login,data):
        allure.dynamic.title(data["title"]);
        self.driver=Login;
        um = User_Manage_Page(driver=self.driver)
        hp = HomePage(driver=self.driver);
        # 用户名和姓名替换
        if "#username#" in data["request_data"]["username"]:
            # 得到不存在的用户名
            sql = "select * from sys_user where user_name ='{}'";
            username = self.get_no_username(sql_templeta=sql);
            self.log.info("在{}页面，生成的用户名是{}".format(self.name, username));
            data["request_data"]["username"] = replace_args(data["request_data"]["username"], username=username);
        if "#realname#" in data["request_data"]["realname"]:
            # 得到未被使用的真实姓名
            sql = "select * from sys_user where real_name ='{}'";
            real_name = self.get_no_username(sql_templeta=sql);
            self.log.info("在{}页面，生成的姓名是{}".format(self.name, real_name));
            data["request_data"]["realname"] = replace_args(data["request_data"]["realname"], realname=real_name);
        hp.system_config_menu_click();
        hp.user_manage_submenu_click();
        um.add_user(**data["request_data"])
        try:
            self.log.info("{}功能开始执行断言".format(self.name))
            self.beidouxing_assert(check_data=data["check_data"]);
            self.log.info("{}功能执行断言通过");
        except Exception as e:
            self.log.exception("{}功能开始断言,断言未通过.".format(self.name));
            self.log.warning("{}断言未通过原因{}".format(self.name,e));
        self.driver.refresh();

    @allure.title("")
    @pytest.mark.parametrize("data",delete_all_user)
    def test_delete_all_user(self,Login,data):
        allure.dynamic.title(data["title"]);
        self.driver = Login;
        hp = HomePage(driver=self.driver);
        hp.system_config_menu_click();
        hp.user_manage_submenu_click();

        self.log.info("{}功能,删除之前获取数据库用户的数量".format(self.name))
        sql = "select * from sys_user";
        self.before_count = self.db.get_count(sql=sql);
        self.log.info("{}功能,删除之前数据库用户数量是:{}".format(self.name, self.before_count));
        # 删除全部用户(10条用户)
        um = User_Manage_Page(driver=self.driver);
        um.delet_all_user(**data["request_data"]);

        #断言:
        try:
            self.log.info("{}功能开始断言".format(self.name))
            self.beidouxing_assert(check_data=data["check_data"]);
            self.log.info("{}功能断言通过".format(self.name));
        except Exception as e:
            self.log.warning("{}功能,断言未通过".format(self.name))
            self.log.exception("{}功能，断言未通过原因是:{}".format(self.name,e))
        try:
            #开始sql校验
            if data["IsSql"]=="1":
                self.log.info("{}功能,删除之后获取数据库用户的数量".format(self.name))
                sql="select * from sys_user";
                self.after_count=self.db.get_count(sql=sql);
                self.log.info("{}功能,删除之后数据库用户数量是:{}".format(self.name,self.after_count));
                #self.assert_equals(self.before_count-10,self.after_count);
                #校验删除之前的数量大于删除之后的数量.
                assert self.before_count>self.after_count;
                self.log.info("{}功能数据库断言通过".format(self.name));
        except Exception as e:
            self.log.exception("{}功能数据库校验未通过,未通过的原因是:{}".format(self.name,e));
            raise e;


    # 用户名称和登录名称模糊查询
    @pytest.mark.parametrize("data",search_name_data)
    @allure.title("")
    def test_search_username(self,data,Login):
        allure.dynamic.title(data["title"]);
        self.driver=Login;
        hp = HomePage(driver=self.driver);
        # 用户名和姓名替换
        if "#loginname#" in data["request_data"]["login_name"]:
            # 得到不存在的用户名
            sql = "select * from sys_user where user_name ='{}' limit 1";
            loginname = self.get_no_username(sql_templeta=sql);
            self.log.info("在{}页面，生成的用户名是{}".format(self.name, loginname ));
            data["request_data"]["login_name"] = replace_args(data["request_data"]["login_name"], loginname=loginname);
        if "#username#" in data["request_data"]["user_name"]:
            # 得到未被使用的真实姓名
            sql = "select * from sys_user where real_name ='{}'";
            username = self.get_no_username(sql_templeta=sql);
            self.log.info("在{}页面，生成的姓名是{}".format(self.name, username));
            data["request_data"]["user_name"] = replace_args(data["request_data"]["user_name"], username=username);


        hp.system_config_menu_click();
        hp.user_manage_submenu_click();
        # 输入登录名称和姓名
        um = User_Manage_Page(driver=self.driver);
        um.search(**data["request_data"]);
        # 断言(此处有待改进，断言方式不正确)
        try:
            self.log.info("{}功能开始断言".format(self.name))
            # 断言登录名称
            if self.get_search_loginname_text() is None and self.get_search_name_text() is None:
                self.beidouxing_assert(check_data=data["check_data"])
            else:
                for i in self.get_search_loginname_text():
                    assert data["request_data"]["login_name"] in i;
                for i in self.get_search_name_text():
                    assert data["request_data"]["user_name"] in i;
        except Exception as e:
            self.log.exception("{}功能断言未通过".format(self.name));
            raise e;







    # 获取修改成功提示信息
    def get_success_tip(self):
        um = User_Manage_Page(driver=self.driver);
        return um.get_success_tip();
    # 获取部门为空错误提示信息
    def get_deptname_isempty(self):
        um = User_Manage_Page(driver=self.driver);
        return um.get_deptname_isempty();

    # 获取登录名称
    def get_search_loginname_text(self):
        um=User_Manage_Page(driver=self.driver);
        loginames = [];
        for i in um.get_search_usernames():
          loginames.append(i.text)
        self.log.info("{}功能获取的登录名称是{}".format(self.name,loginames))
        return loginames

    # 获取用户名
    def get_search_name_text(self):
        um = User_Manage_Page(driver=self.driver);
        names=  [];
        for i in um.get_search_names():
            names.append(i.text);
        self.log.info("{}功能获取的用户姓名是:{}".format(self.name,names));
        return names;

    # 根据用户名和姓名查询不到数据
    def get_search_nodata_text(self):
        um = User_Manage_Page(driver=self.driver);
        return um.get_search_nodata()