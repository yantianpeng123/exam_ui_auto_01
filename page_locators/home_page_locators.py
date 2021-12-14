#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/10/17  下午2:05
# @Author  : yantianpeng
# @Site    : 
# @File    : home_page_locators.py
# @Software: PyCharm
'''
from selenium.webdriver.common.by import By
class HomePageLocator(object):


    #获取首页欢迎使用
    wel_text_loc = (By.XPATH,'//div[contains(text(),"欢迎使用")]');

    # 在线考试菜单栏
    online_exam_menu_loc = (By.XPATH,"//div[@class='el-submenu__title']//span[text()='在线考试']")
    # 在线考试子菜单栏
    online_exam_submenu_loc =(By,"//a[@href='#/my/exam']");
    # 我的成绩子菜单栏
    my_exam_score_submenu_loc = (By.XPATH,'//a[@href="#/my/exam/records"]');

    #考试管理
    exam_manag_menu_loc = (By.XPATH,'//div[@class=\'el-submenu__title\']//span[text()="考试管理"]');

    #考试管理(子菜单栏)
    exam_manage_submenu_loc=(By.XPATH,"//a[@href='#/exam/exam']");
    #题库管理
    ques_manage_submenu_loc = (By.XPATH,'//li[@role="menuitem"]//span[text()="题库管理"]');
    #试题管理
    qu_manage_submenu_loc =(By.XPATH,'//li[@role="menuitem"]//span[text()="试题管理"]');

    # 系统配置
    system_config_menu_loc=(By.XPATH,'//span[text()="系统设置"]');
    # 系统配置
    system_config_submenu_loc = (By.XPATH,"//span[text()='系统配置']");
    # 部门管理
    dept_manage_submenu_loc =(By.XPATH,'//span[text()="部门管理"]');
    # 角色管理
    role_manage_submenu_loc =(By.XPATH,'//span[text()="角色管理"]');
    #用户管理
    users_manage_submenu_loc =(By.XPATH,"//span[text()='用户管理']");


    #退出之前的三角
    index_icon_loc = (By.XPATH,"//i[@class='el-icon-caret-bottom']");

    #退出登录
    login_out_loc = (By.XPATH,"//span[text()='退出登录']");


