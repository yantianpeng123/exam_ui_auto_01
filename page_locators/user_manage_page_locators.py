#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/10/19  下午10:41
# @Author  : yantianpeng
# @Site    : 
# @File    : user_manage_page_locators.py
# @Software: PyCharm
'''
from selenium.webdriver.common.by import By
class   UserManageLocators(object):

    #搜索登录名
    search_login_name_input_loc =(By.XPATH,"//input[@placeholder='搜索登录名']");
    #搜索用户名
    search_username_input_loc =(By.XPATH,"//input[@placeholder='搜索姓名']");
    #添加用户按钮
    add_user_btn_loc= (By.XPATH,"//button[@type='button']//span[contains(text(),'添加')]");

    # 复选框(选中所有的元素)
    checkboxs_btn_loc=(By.XPATH,'//th[@colspan="1"]//div[text()="用户名"]/preceding::th//span//span');

    #选择下拉框
    select_btn_loc = (By.XPATH,'//input[contains(@placeholder,"已选")]');

    # 弹出框
    alter_loc =(By.XPATH,"//div[@class='el-message-box']");

    # 删除按钮/选择框
    del_user_btn_loc=(By.XPATH,'//span[text()="删除"]');

    #确定按钮
    add_user_accept_btn_loc = (By.XPATH,"//span[contains(text(),'确 定')]");
    # 删除按钮
    del_user_accpet_btn_loc = (By.XPATH,"//span[contains(text(),'确定')]");
    #用户名
    add_user_name_input_loc =(By.XPATH,"//label[text()='用户名']/following-sibling::div//input");
    #姓名
    add_user_realname_input_loc =(By.XPATH,"//label[text()='姓名']/following-sibling::div//input")
    # 密码
    #add_user_password_input_loc =(By.XPATH,"//label[text()='密码']/following-sibling::div//input")
    # placeholder="不修改请留空"
    add_user_password_input_loc = (By.XPATH,"//input[contains(@placeholder,'不修改请留空')]")

    #部门
    add_user_dept_btn_loc =(By.XPATH,"//label[text()='部门']/following-sibling::div//input");
    #角色 //input[@placeholder="请选择角色"]/following-sibling::span//i
    # add_user_role_btn_loc =(By.XPATH,'//input[@placeholder="请选择角色"]');
    add_user_role_btn_loc=(By.XPATH,'//input[@placeholder="请选择角色"]/following-sibling::span//i')
    # 选择角色
    check_stu_role_btn_loc= (By.XPATH,"//span[text()='student']")
    check_sa_role_btn_loc =(By.XPATH,"//span[text()='sa']");

    # 选择技术部门
    check_dept_btn_loc = (By.XPATH,'//div[@placeholder="选择部门"]//span[text()="技术部"]');
    # 选择第四个部门
    check_dept_four_btn_loc =(By.XPATH,'//div[@placeholder="选择部门"]//div[4]');

    # 选择第一个部门:
    check_dept_btn_first_loc=(By.XPATH,"//span[@class='el-tree-node__label']");

    #修改/删除提示信息
    user_manage_success_tip_loc=(By.XPATH,"//p[@class='el-message__content']");
    # 部门数据不存在提示信息
    deptname_isempty_tip_loc =(By.XPATH,"//span[@class='el-tree__empty-text']")


    #删除指定的用户
    delet_one_user_btn_loc= (By.XPATH,"//tr[@class='el-table__row'][1]//span[@class='el-checkbox__inner']")

    #获取登录名称内容
    search_username_input = (By.XPATH,"//div[@class='cell']/a");

    #获取姓名
    search_name_input= (By.XPATH,'//td[contains(@class,"el-table_1_column_3")]');



