#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/10/20  下午3:46
# @Author  : yantianpeng
# @Site    : 
# @File    : user_manage_datas.py
# @Software: PyCharm
'''
user_manage_success=[
    {
        "title":"添加成功",
        "request_data":{"username":"#username#","realname":"#realname#","password":"admin","role":"sa","dept":"1"},
        "check_data":{"method":"get_success_tip","value":"用户修改成功!"},
        "IsSql":"1",
    },{
        "title":"添加成功--用户名为空",
        "request_data":{"username":" ","realname":"#realname#","password":"admin","role":"sa","dept":"1"},
        "check_data":{"method":"get_success_tip","value":"用户修改成功!"},
        "IsSql":"1",
    },
    {
        "title":"添加成功--用户名为空格",
        "request_data":{"username":"","realname":"#realname#","password":"admin","role":"sa","dept":"1"},
        "check_data":{"method":"get_success_tip","value":"用户修改成功!"},
        "IsSql":"1",
    },
    #姓名
    {
        "title":"添加成功--姓名为空",
        "request_data":{"username":"#username#","realname":" ","password":"admin","role":"sa","dept":"1"},
        "check_data":{"method":"get_success_tip","value":"用户修改成功!"},
        "IsSql":"1",
    },
    {
        "title":"添加成功--姓名为空格",
        "request_data":{"username":"#username#","realname":"","password":"admin","role":"sa","dept":"1"},
        "check_data":{"method":"get_success_tip","value":"用户修改成功!"},
        "IsSql":"1",
    },
    #密码
    {
        "title":"添加成功--密码为空",
        "request_data":{"username":"#username#","realname":"#realname#","password":"","role":"sa","dept":"1"},
        "check_data":{"method":"get_success_tip","value":"用户修改成功!"},
        "IsSql":"1",
    },
    {
        "title":"添加成功--密码为空格",
        "request_data":{"username":"#username#","realname":"#realname#","password":" ","role":"sa","dept":"1"},
        "check_data":{"method":"get_success_tip","value":"用户修改成功!"},
        "IsSql":"1",
    },
    #角色为空
    {
        "title":"添加失败--角色为空格",
        "request_data":{"username":"#username#","realname":"#realname#","password":"admin","role":"","dept":"1"},
        "check_data":{"method":"get_success_tip","value":"至少要包含一个角色！"},
        "IsSql":"0",#不进行sql校验
    },
    {
        "title":"添加成功--角色为空",
        "request_data":{"username":"#username#","realname":"#realname#","password":"admin","role":" ","dept":"1"},
        "check_data":{"method":"get_success_tip","value":"至少要包含一个角色！"},
        "IsSql":"0",#不进行sql校验
    }
]

fail_deptname_isempty=[
    {
        "title":"添加失败--部门为空",
        "request_data":{"username":"#username#","realname":"#realename#","password":"admin","role":"sa","dept":"0"},
        "check_data":{"method":"get_deptname_isempty","value":"暂无数据"}
    }
]

# 删除全选/单选用户
delete_all_user=[
    {
        "title":"删除全选用户",
        "request_data":{"index":"0"},
        "check_data":{"method":"get_success_tip","value":"删除成功!"},
        "IsSql":"1",#进行sql校验
    },
    {
        "title":"删除单选用户",
        "request_data":{"index":"1"},
        "check_data":{"method":"get_success_tip","value":"删除成功!"},
        "IsSql":"1",#进行sql校验
    }
]

# 用户名称和登录名称模糊查询
search_name_data=[
    {
        "title":"模糊查询",
        "request_data":{"login_name":"n","user_name":"n"},
        "check_data":{"method":"get_search_text"},
        "IsSql":"0"
    },
    {
        "title":"登录名称不存在",
        "request_data":{"login_name":"#loginname#","user_name":"n"},
        "check_data":{"method":"get_search_nodata_text","value":"暂无数据"},
        "IsSql":"0"
    },
    {
        "title":"用户名称不存在",
        "request_data":{"login_name":"n","user_name":"#username#"},
        "check_data":{"method":"get_search_nodata_text","value":"暂无数据"},
        "IsSql":"0"
    },
    {
        "title":"登录名称和用户名称都不存在",
        "request_data":{"login_name":"#loginname#","user_name":"#username#"},
        "check_data":{"method":"get_search_nodata_text","value":"暂无数据"},
        "IsSql":"0"
    },
]