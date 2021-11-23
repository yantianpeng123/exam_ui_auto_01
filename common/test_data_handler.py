#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/10/18  上午9:48
# @Author  : yantianpeng
# @Site    : 
# @File    : test_data_handler.py
# @Software: PyCharm
'''
#处理测试数据
import random

def get_username():
    username=["y_"];
    for i in range(5):
        username.append(random.choice("qwertyuiopasdfghjklzxcvbnm"))
    return "".join(username);


def replace_args(fs,flag ='#',**kwargs):
    """

    :param fs:
    :param kwargs:
    :return:
    """
    for args ,values in  kwargs.items():
         fs = fs.replace("{0}{1}{0}".format(flag,args),str(values));
    return fs;