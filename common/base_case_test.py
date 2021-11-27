#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/10/4  下午5:34
# @Author  : yantianpeng
# @Site    : 
# @File    : base_case_test.py
# @Software: PyCharm
'''
from common.beidouxing_mysql_handler import db
from common.test_data_handler import get_username,get_deptname
from common.loging_handler import log;
import setting
class BaseCase(object):

    name= None;
    log=log
    setting=setting;
    db=db;

    @classmethod
    def setup_class(cls):
        cls.log.info("=====>{}:开始执行测试<====".format(cls.name));

    @classmethod
    def teardown_class(cls):
        cls.log.info("=====>{}:执行测试结束<=====".format(cls.name));




    def beidouxing_assert(self,check_data,msg='XX功能'):
        """
        自定义断言
        :return:
        """
        method = getattr(self,check_data["method"])
        res= method();
        try:
            self.assert_equals(res, check_data['value'], msg)
        except Exception as e:
            self.log.exception("{}:断言失败".format(msg));
            self.log.warning("测试函数返回的实际结果是:{}".format(res));
            self.log.warning("期望结果是:{}".format(check_data['value']));
            raise e;
        else:
            self.log.info("{}:断言成功".format(msg))


    def assert_equals(self,first,second,msg=""):
        """
        断言是否相等
        :param first:
        :param second:
        :param msg:
        :return:
        """
        if first!=second:
            if msg:
                raise AssertionError(msg);

            else:
                raise  AssertionError("{}!={}".format(first,second));


    def get_no_username(self,sql_templeta):
        while True:
            username = get_username()
            if not self.db.Isexit(sql=sql_templeta.format(username)):
                return username;


    def get_no_deptname(self,sql_templeta):
        while True:
            deptname = get_deptname();
            if not self.db.Isexit(sql=sql_templeta.format(deptname)):
                return deptname;