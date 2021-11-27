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
class Dept_Manage_Page(BasePage):
    name = "用户管理界面";


    def search_dept(self,deptname):
        """
        根据部门名称查询部门
        :param depaname:
        :return:
        """
        self.wait_element_presence_located(DeptPageLocator.search_dept_input,action="输入部门名称").send_keys(content=deptname);


    def add_dept(self,deptname):
        """
        输入部门名称
        :param deptname:
        :return:
        """
        self.wait_element_presence_located(DeptPageLocator.add_dept_btn,action="点击添加部门按钮").click_element();
        self.wait_element_presence_located(DeptPageLocator.plus_dept_input,action="输入部门名称").send_keys(content=deptname);
        self.wait_element_presence_located(DeptPageLocator.plus_dept_accept_btn,action="点击确定按钮").click_element();



    def delete_dept(self,index=0):
        """
        删除部门 默认删除第一个
        :param index:
        :return:
        """
        element = self.find_elements(DeptPageLocator.delete_dept_btns);
        element[index].click();
        self.wait_element_presence_located(DeptPageLocator.plus_dept_accept_btn,action="点击确定按钮").click_element();


    def edit_dept(self,index=0):
        """
        编辑部门
        :param index:
        :return:
        """
        element = self.find_elements(DeptPageLocator.edit_dept_btns);
        element[index].click();
        self.wait_element_presence_located(DeptPageLocator.plus_dept_accept_btn,action="点击确定按钮").click_element();


    def add_plus_dept(self,index=0):
        """
        新增子部门，默认新增的是第一个部门.
        :param index:
        :return:
        """
        element = self.find_elements(DeptPageLocator.plus_dept_btns);
        element[index].click();
        self.wait_element_presence_located(DeptPageLocator.plus_dept_accept_btn,action="点击确定按钮").click_element();

