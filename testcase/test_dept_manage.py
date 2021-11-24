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
import allure
import pytest

class TestDeptManage(BaseCase):

    name = "部门管理";

    @allure.title("")
    @pytest.mark.parametrize("data",)
    def test_add_dept(self,Login,data):
        allure.dynamic.title(data["title"]);
        self.driver= Login;
        pass;

    @allure.title("")
    @pytest.mark.parametrize("data",)
    def test_delete_dept(self,Login,data):
        allure.dynamic.title(data["title"]);
        pass

    @allure.title("")
    @pytest.mark.parametrize("data")
    def test_edit_dept(self,Login,data):
        allure.dynamic.title(data["title"])
        pass;
