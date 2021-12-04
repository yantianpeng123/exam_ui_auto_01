#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/11/24  下午11:35
# @Author  : yantianpeng
# @Site    : 
# @File    : dept_manage_page_locators.py
# @Software: PyCharm
'''
from selenium.webdriver.common.by import By
class DeptPageLocator(object):
    # 公司名称搜索
    search_dept_input_loc = (By.XPATH,"//input[@placeholder='搜索公司名称']")

    # 添加按钮
    # //button//span[contains(text(),"添加")]
    # // button // span[contains(text(), '添加')] // parent::button // i
    add_dept_btn_loc =  (By.XPATH,"//button//span[contains(text(),'添加')]//parent::button//i");

    # 删除按钮 查找多个元素
    delete_dept_btns_loc = (By.XPATH,"//i[@class='el-icon-delete']");

    #编辑按钮 查找多个元素
    edit_dept_btns_loc = (By.XPATH,"//i[@class='el-icon-edit']");

    #维护部门(新增子部门) 查找多个元素
    plus_dept_btns_loc = (By.XPATH,"//i[@class='el-icon-plus']");

    # 维护部门 输入部门名称
    plus_dept_input_loc = (By.XPATH,'//label[text()="部门名称"]//following-sibling::div//input');

    # 维护部门 确定按钮
    # //span[contains(text(),'确 定')]//parent::button
    # //span[contains(text(),'确 定')]
    plus_dept_accept_btn_loc = (By.XPATH,"//span[contains(text(),'确 定')]//parent::button");
    # 维护部门 取消按钮
    plus_dept_cancel_btn_loc = (By.XPATH,"//span[contains(text(),'取 消')]");


    # 搜索部门名称表格
    search_dept_name_tables_loc= (By.XPATH,'//td[contains(@class,"el-table_1_column_1")]//div');


    # 当搜索不到部门元素定位
    search_no_dept_loc=(By.XPATH,"//span[@class='el-table__empty-text']");


    # 添加部门成功提示
    add_dept_success_tip = (By.TAG_NAME,"h2");


    # 添加部门失败提示
    add_dept_fail_tip = (By.XPATH,"//div[@class='el-form-item__error']");