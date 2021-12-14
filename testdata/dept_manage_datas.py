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


add_dept_datas=[
    {
        "title":"新增部门--部门不为空",
        "request_data":{"deptname":"#deptname#"},
        "check_data":{"method":"get_add_tip","value":"成功"},
        "IsSql":"1"
    },
]

fail_add_dept_datas=[
    {
        "title":"新增部门--部门为空",
        "request_data":{"deptname":""},
        "check_data":{"method":"get_no_deptname_tip","value":"部门名称不能为空！"},
        "IsSql":"1"
    }
]

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

delete_dept = [
    {
        "title":"删除部门",
        "request_data":{"index":0},
        "check_data":{"method":"","value":"删除成功"}
    }
]



edit_dept_datas =[
    {
        "title":"编辑部门--部门名称不一样",
        "request_data":{"deptname":"#deptname#"},
        "check_data":{"method":"get_add_tip","value":"成功"},
        "IsSql":"1"
    },
    {
        "title":"编辑部门--部门为空",
        "request_data":{"deptname":""},
        "check_data":{"method":"get_no_deptname_tip","value":"部门名称不能为空！"}
    }
]