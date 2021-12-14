#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/11/27  下午9:02
# @Author  : yantianpeng
# @Site    : 
# @File    : Dept_Manage_Page.py
# @Software: PyCharm
'''
from page_object.base_page import BasePage;
from page_locators.dept_manage_page_locators import DeptPageLocator;
from time import sleep
class Dept_Manage_Page(BasePage):
    name = "用户管理界面";


    def search_dept(self,deptname):
        """
        根据部门名称查询部门
        :param depaname:
        :return:
        """
        self.wait_element_presence_located(DeptPageLocator.search_dept_input_loc,action="输入部门名称").send_keys(content=deptname);


    def add_dept(self,deptname):
        """
        输入部门名称
        :param deptname:
        :return:
        """
        self.wait_element_presence_located(DeptPageLocator.add_dept_btn_loc,action="点击添加部门按钮").click_element();
        self.wait_element_presence_located(DeptPageLocator.plus_dept_input_loc,action="输入部门名称").send_keys(content=deptname);
        sleep(2);
        self.wait_element_presence_located(DeptPageLocator.plus_dept_accept_btn_loc,action="点击确定按钮").click_element()



    def delete_dept(self,index=0):
        """
        删除部门 默认删除第一个
        :param index:
        :return:
        """
        element = self.find_elements(DeptPageLocator.delete_dept_btns_loc);
        element[index].click();
        self.wait_element_presence_located(DeptPageLocator.plus_dept_accept_btn_loc,action="点击确定按钮").click_element();


    def edit_dept(self,deptname,index=0):
        """
        编辑部门
        :param index:
        :return:
        """
        element = self.find_elements(DeptPageLocator.edit_dept_btns_loc);
        element[index].click();
        # 输入部门名称
        self.wait_element_presence_located(DeptPageLocator.plus_dept_input_loc,action="输入部门名称").send_keys(content=deptname);
        self.wait_element_presence_located(DeptPageLocator.plus_dept_accept_btn_loc,action="点击确定按钮").click_element();


    def add_plus_dept(self,index=0):
        """
        新增子部门，默认新增的是第一个部门.
        :param index:
        :return:
        """
        element = self.find_elements(DeptPageLocator.plus_dept_btns_loc);
        element[index].click();
        self.wait_element_presence_located(DeptPageLocator.plus_dept_accept_btn_loc,action="点击确定按钮").click_element();


    def get_dept_name_tables(self):
        """获取部门名称表格"""
        return self.find_elements(DeptPageLocator.search_dept_name_tables_loc);



    def get_no_dept_data(self):
        return self.wait_element_presence_located(DeptPageLocator.search_no_dept_loc,action="查询不存在的部门元素定位");


    def get_add_tip(self):
        return self.wait_element_presence_located(DeptPageLocator.add_dept_success_tip,action="获取添加部门成功提示");

    def get_no_deptname_tip(self):
        return self.wait_element_presence_located(DeptPageLocator.add_dept_fail_tip,action="获取部门为空提示");