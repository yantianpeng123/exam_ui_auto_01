#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/10/17  上午11:14
# @Author  : yantianpeng
# @Site    : 
# @File    : conftest.py
# @Software: PyCharm
'''
import pytest
from selenium import webdriver
from page_object.login_page import Login_Page
from page_object.home_page import HomePage
import setting
@pytest.fixture(scope="class")
def driver():
    """
    实例化浏览器驱动
    :return:
    """
    with webdriver.Chrome(executable_path="/Users/yantianpeng/Downloads/chromedriver") as wd:
        wd.maximize_window()

        wd.get(setting.PROJECT_HOST_VUE)
        yield wd;
        wd.quit();


@pytest.fixture(scope="class")
def Login(driver):
    Login_Page(driver=driver).login(**setting.ADMIN_INFO);
    yield driver;


@pytest.fixture(scope="class")
def systemconfig(Login):
    hp=HomePage(driver=driver)
    hp.system_config_menu_click();
    yield driver;
