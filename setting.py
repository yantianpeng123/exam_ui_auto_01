#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8
'''
# @Time    : 2021/10/4  下午5:34
# @Author  : yantianpeng
# @Site    : 
# @File    : setting.py
# @Software: PyCharm
'''
import os

# 项目根路径
BASE_PATH = os.path.dirname(os.path.abspath(__file__));

# 测试用例的路径
TEST_CASE_DIR =  os.path.join(BASE_PATH,'testcase');

# 项目路径
PROJECT_HOST_VUE = "http://81.68.203.75:8101/";

# 存放测试报告的路径
ALLURE_RESULT_DIR = os.path.join(BASE_PATH,"report");

# 元素查找超时时间
DEFAULT_TIMEOUT = 3;

# 错误截图路径
ERROR_SCREENSHOT_DIR = os.path.join(BASE_PATH,'screehot');


ADMIN_INFO={"username":"admin","password":"admin"};

# 日志配置
LOG_CONFIG={
    "file":os.path.join("./log/beidouxing.log"),
    "format":"%(asctime)s-->[%(filename)s-->%(levelname)s-->行号:%(lineno)s-->日志信息:%(message)s]",
    "datefmt":'%Y-%m-%d %I:%M:%S',
    "debug":False
}

MYSQL_CONFIG={
    "host": "81.68.203.75",
     "port": 3307,
     "user": "root",
     "password": "beidouxing@888",
     "db": "yf_exam_lite",
     "autocommit": True, #解决可重复的
     "charset": "utf8"
}