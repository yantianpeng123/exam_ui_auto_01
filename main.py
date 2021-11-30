#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/10/4  下午5:34
# @Author  : yantianpeng
# @Site    : 
# @File    : main.py
# @Software: PyCharm
'''
import setting
import pytest
import os
if __name__ == '__main__':
    pytest.main([
        "-v",
        "-s",
        os.path.join(setting.TEST_CASE_DIR,"test_dept_manage.py"),
        "--alluredir={}".format(setting.ALLURE_RESULT_DIR),
        "--clean-alluredir"
    ])

os.system("allure serve {}".format(setting.ALLURE_RESULT_DIR));