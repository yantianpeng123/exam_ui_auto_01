#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8
'''
# @Time    : 2021/11/24  下午11:34
# @Author  : yantianpeng
# @Site    : 
# @File    : dept_manage_datas.py
# @Software: PyCharm
'''

success_datas= [

    {
        "title":"查询部门--存在的部门",
        "request_data":{"deptname":"5"}
    }
]

success_no_datas=[
    {
        "title": "查询部门--未存在的部门",
        "request_data": {"deptname": "#deptname#"},
        "check_data": {"method": "get_no_dept_name", "value": "暂无数据"}
    }
]