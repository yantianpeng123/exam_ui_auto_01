#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/10/17  下午10:52
# @Author  : yantianpeng
# @Site    : 
# @File    : beidouxing_mysql_handle.py
# @Software: PyCharm
'''
import pymysql
import setting
class Beidouxing_MysqlDB(object):

    def __init__(self,**kwargs):
        self.con =pymysql.connect(**kwargs);
        self.cur =self.con.cursor(pymysql.cursors.DictCursor);# 返回是字典


    def Isexit(self,sql):
        """
            判断某一些数据是否存在
        :param sql:
        :return:
        """
        self.cur.execute(sql);
        if self.cur.fetchone():
            return True;
        return False;


    def get_one_data(self,sql):
        """
        获取一条数据
        :param sql:
        :return:
        """
        self.cur.execute(sql);
        return self.cur.fetchone();

    def get_many_data(self,sql,size):
        """
        获取制定条数的数据
        :param sql:
        :param size:
        :return:
        """
        self.cur.execute(sql);
        self.cur.fetchmany(size=size);

    def get_all_data(self,sql):
        """
        返回全部数据
        :param sql:
        :return:
        """
        self.cur.execute(sql);
        return self.cur.fetchall();

    def get_count(self,sql):
        """
        返回查询结果的条数
        :param sql:
        :return:
        """
        return self.cur.execute(sql);

    def inert_data(self,sql):
        try:
            self.cur.execute(sql);
            self.con.commit();
        except :
            self.con.rollback();
        finally:
            self.cur.close();
            self.con.close();


    def __del__(self):
        self.cur.close();
        self.con.close();

db= Beidouxing_MysqlDB(**setting.MYSQL_CONFIG)

# sql="select * from sys_user where user_name like\"yantianpeng%\";";
#
# ss =db.get_one_data(sql=sql);
# print(ss)