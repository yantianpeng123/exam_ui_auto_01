#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/10/19  下午11:37
# @Author  : yantianpeng
# @Site    : 
# @File    : user_manage_page.py
# @Software: PyCharm
'''
from page_object.base_page import BasePage
from page_locators.user_manage_page_locators import UserManageLocators
class User_Manage_Page(BasePage):

    name = "用户管理页面";

    def search(self,login_name,user_name):
        self.wait_element_presence_located(UserManageLocators.search_login_name_input_loc,action="输入登录名称").send_keys(content=login_name);
        self.wait_element_presence_located(UserManageLocators.search_username_input_loc,action="输入用户名").send_keys(content=user_name);


    def search_login(self,login_name):
        self.wait_element_presence_located(UserManageLocators.search_login_name_input_loc,action="输入登录名称").send_keys(content=login_name);

    def search_username(self,username):
        self.wait_element_presence_located(UserManageLocators.search_username_input_loc,action="输入用户名").send_keys(content=username);


    def add_user(self,username,realname,password,role='sa',dept="1"):
        # 添加按钮
        self.wait_time(0.5)
        self.wait_element_to_be_clicked(UserManageLocators.add_user_btn_loc,action="点击添加按钮").click_element();
        # 输入用户名
        self.wait_element_presence_located(UserManageLocators.add_user_name_input_loc,action="输入用户名").send_keys(content=username);
        self.wait_element_presence_located(UserManageLocators.add_user_role_btn_loc, action="点击选择角色").click_element();
        # 选择角色
        self.wait_time(1)
        if "sa" == role:
            self.wait_element_presence_located(UserManageLocators.check_sa_role_btn_loc,action="选择管理员角色").click_element();
        elif "student" ==role:
            self.wait_element_presence_located(UserManageLocators.check_stu_role_btn_loc,action="选择学生角色").click_element();
        elif ""==role or " "==role or None is role:
            #self.wait_element_presence_located(UserManageLocators.check_stu_role_btn_loc,action="选择学生角色").click_element();
            #self.wait_element_presence_located(UserManageLocators.check_sa_role_btn_loc,action="选择管理员角色").click_element();
            pass;
        elif "all"==role:
            self.wait_element_presence_located(UserManageLocators.check_sa_role_btn_loc,
                                               action="选择管理员角色").click_element();
            self.wait_element_presence_located(UserManageLocators.check_stu_role_btn_loc,
                                               action="选择学生角色").click_element();
        #输入姓名
        self.wait_element_presence_located(UserManageLocators.add_user_realname_input_loc,action="点击用户名输入款").click_element();
        self.wait_element_presence_located(UserManageLocators.add_user_realname_input_loc,action="输入姓名").send_keys(content=realname);
        #输入密码
        self.wait_element_presence_located(UserManageLocators.add_user_password_input_loc,action="输入密码").send_keys(content=password);
        # 选择部门
        self.wait_element_presence_located(UserManageLocators.add_user_dept_btn_loc,action="点击选择部门").click_element();

        # 选在具体的部门
        if "0"==dept:
            self.wait_element_presence_located(UserManageLocators.add_user_dept_btn_loc,
                                               action="点击选择部门").send_keys("y_admin");
        else:
            # self.wait_element_presence_located(UserManageLocators.check_dept_btn_loc,action="选择技术部门").click_element();
            self.find_elements(locator=UserManageLocators.check_dept_btn_first_loc)[0].click();
            self.wait_time(2)
            self.wait_element_presence_located(UserManageLocators.add_user_accept_btn_loc,action="点击确定按钮").click_element();

    def delet_all_user(self,index="2"):
        # 点击全选按钮
        if index=="0":
            self.wait_element_to_be_clicked(UserManageLocators.checkboxs_btn_loc,action="点击全选按钮").click_element();
        else:
            #UserManageLocators.delet_one_user_btn_loc.format(index);
            self.wait_element_presence_located(UserManageLocators.delet_one_user_btn_loc,action="删除指定的用户").click_element();
        # 选择删除
        self.wait_element_presence_located(UserManageLocators.select_btn_loc,action='').click_element();
        self.wait_time(1);
        self.wait_element_presence_located(UserManageLocators.del_user_btn_loc,action="选择删除选项").click_element();
        self.wait_time(1); #66631
        self.wait_element_presence_located(UserManageLocators.del_user_accpet_btn_loc,action="删除操作点击确认,点击确定").click_element();



    def get_success_tip(self):
        """
        获取用户修改成功提示
        :return:
        """
        return self.wait_element_presence_located(UserManageLocators.user_manage_success_tip_loc,action="获取修改成功信息").get_element_text();


    def get_deptname_isempty(self):
        """
        获取部门数据不存在提示信息
        :return:
        """
        return self.wait_element_presence_located(UserManageLocators.deptname_isempty_tip_loc,action="获取部门数据不存在提示信息").get_element_text()


    def get_search_usernames(self):
        """
        获取登录名称
        :return:
        """
        return self.find_elements(UserManageLocators.search_username_input);

    def get_search_names(self):
        """
        获取用户姓名
        :return:
        """

        return self.find_elements(UserManageLocators.search_name_input);