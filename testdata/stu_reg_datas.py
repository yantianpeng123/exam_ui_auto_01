#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/10/17  下午10:27
# @Author  : yantianpeng
# @Site    : 
# @File    : stu_reg_datas.py
# @Software: PyCharm
'''
success_data=[
    {
        "title":"注册成功",
        "request_data":{"username":"#username#","realname":"#realname#","password":"admin1"},
        "check_data":{"method":"is_login","value":True}
    },
    {
        "title":"注册成功--用户姓名为空格",
        "request_data":{"username":"#username#","realname":"  ","password":"admin1"},
        "check_data":{"method":"is_login","value":True}
    }
]

fail_data_userexist=[
    {
        "title":"注册失败--用户已存在",
        "request_data":{"username":"#username#","realname":"#realname#","password":"admin1"},
        "check_data":{"method":"get_error_alter_tip","value":"用户名已存在，换一个吧！"}
    }
]

fail_data_user_error=[
    {
        "title":"注册失败--用户名空",
        "request_data":{"username":"","realname":"realname","password":"admin1"},
        "check_data":{"method":"get_error_tip","value":"用户名不能小于5个字符"}
    },
    {
        "title":"注册失败--用户名空格",
        "request_data":{"username":" ","realname":"realname","password":"admin1"},
        "check_data":{"method":"get_error_tip","value":"用户名不能小于5个字符"}
    },
    {
        "title":"注册失败--小于五个字符",
        "request_data":{"username":"aa","realname":"realname","password":"admin1"},
        "check_data":{"method":"get_error_tip","value":"用户名不能小于5个字符"}
    }
]

fail_data_realname_error=[
    {
        "title":"注册失败--姓名为空",
        "request_data":{"username":"admin1","realname":"","password":"admin"},
        "check_data": {"method": "get_error_tip", "value": "用户姓名不能为空！"}
    }
]

fail_data_pwd_error=[
    {
        "title": "注册失败--密码为空",
        "request_data": {"username": "admin", "realname": "realname", "password": ""},
        "check_data": {"method": "get_error_tip", "value": "密码不能小于5个字符"}
    },
    {
        "title": "注册失败--密码为空格",
        "request_data": {"username": "admin", "realname": "realname", "password": " "},
        "check_data": {"method": "get_error_tip", "value": "密码不能小于5个字符"}
    },
    {
        "title":"注册测试--密码小于五个字符",
        "request_data":{"username":"admin","realname":"realname","password":"as"},
        "check_data":{"method":"get_error_tip","value":"密码不能小于5个字符"}
    }
]
