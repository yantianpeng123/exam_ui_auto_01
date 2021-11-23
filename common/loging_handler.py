#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/10/5  下午2:53
# @Author  : yantianpeng
# @Site    : 
# @File    : loging_handler.py
# @Software: PyCharm
'''

import setting
import  logging
from logging import handlers

"""
日志封装
"""
def get_log(name=__name__,file='../log.log',
            format="%(asctime)s-->[%(filename)s-->%(levelname)s-->行号:%(lineno)s-->日志信息:%(message)s]",
            datefmt = '%Y-%m-%d %I:%M:%S',debug=False):

    if debug:
        file_level = logging.DEBUG;
        console_level = logging.DEBUG;
    else:
        file_level = logging.INFO;
        console_level = logging.INFO;
    #设置日志记录器
    log = logging.getLogger(name);

    #设置日志级别
    log.setLevel(logging.DEBUG);

    #创建日志处理器
    #输出到文件
    file_handle = logging.FileHandler(filename=file);
    file_handle.setLevel(file_level);

    #输出到控制台
    console_handle = logging.StreamHandler();
    console_handle.setLevel(console_level);

    #设置日志轮询 特定时间生成日志 这需要保持项目的持续运行才可以生成
    th = handlers.TimedRotatingFileHandler(filename=file,when='D');
    th.setLevel(logging.DEBUG);
    #设置文件前缀
    th.suffix = "%Y-%m-%d.log"

    #日志格式化器
    fmt = logging.Formatter(fmt=format,datefmt=datefmt);

    file_handle.setFormatter(fmt=fmt);
    console_handle.setFormatter(fmt=fmt);
    th.setFormatter(fmt=fmt);

    log.addHandler(file_handle);
    log.addHandler(console_handle);
    log.addHandler(th);

    return log;

log =  get_log(**setting.LOG_CONFIG);

log.info("sss")