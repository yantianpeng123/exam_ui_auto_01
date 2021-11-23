#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/10/19  下午4:22
# @Author  : yantianpeng
# @Site    : 
# @File    : sys_config_datas.py
# @Software: PyCharm
'''

sys_config_data=[
    {
        "title":"保存成功--系统名字为空",
        "request_data":{"sysname":""},
        "check_data":{"method":"get_success_tip","value":"成功"}
    },
    {
        "title":"保存成功--系统名字为字符串",
        "request_data":{"sysname":"北斗星考试系统"},
        "check_data":{"method":"get_success_tip","value":"成功"}
    }
]