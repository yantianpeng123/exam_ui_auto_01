#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/10/17  上午11:18
# @Author  : yantianpeng
# @Site    : 
# @File    : test_login_data.py
# @Software: PyCharm
'''
#测试用例
#正向用例
success_data =[
    {
        "title":"登录成功",
        "request_data":{"username":"admin","password":"admin"},
        "check_data":{"method":"is_login","value":True}
    }
]

fail_data=[
    {
        "title":"登录失败--账号错误",
        "request_data":{"username":"admin1","password":"admin"},
        "check_data":{"method":"get_error_username_pwd_tip","value":"管理员账号不存在！"}
    },
    {
    "title":"登录失败--账号为空",
    "request_data":{"username":" ","password":"admin"},
    "check_data":{"method":"get_error_username_pwd_tip","value":"账号或密码错误！"}
    },
    {
      "title":"登录失败--密码错误-且长度大于5个字符",
      "request_data":{"username":"admin","password":"admin1"},
      "check_data":{"method":"get_error_username_pwd_tip","value":"账号或密码错误！"}
    }
]
fail_data_pwd_notlen=[
    {
        "title":"登录失败--密码长度不足",
        "request_data":{"username":"admin1","password":"as"},
        "check_data":{"method":"get_error_pwd_not_enough","value":"密码不能小于5个字符"}
    },
    {
        "title":"登录失败--密码为空",
        "request_data":{"username":"admin1","password":""},
        "check_data":{"method":"get_error_pwd_not_enough","value":"密码不能小于5个字符"}
    },
    {
        "title":"登录失败--密码为空格",
        "request_data":{"username":"admin1","password":" "},
        "check_data":{"method":"get_error_pwd_not_enough","value":"密码不能小于5个字符"}
    }
]