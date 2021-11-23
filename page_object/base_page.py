#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/10/5  下午2:51
# @Author  : yantianpeng
# @Site    : 
# @File    : base_page.py
# @Software: PyCharm
'''
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait;
from selenium.webdriver.support  import expected_conditions as EC;
from selenium.webdriver.support.select import Select
from datetime import datetime
from time import sleep
import os;
from common.loging_handler import log
import setting

"""
 页面基础类
"""
class BasePage(object):
    name = "Base页面";
    log = log;
    setting=setting;


    def __init__(self,driver:webdriver):
        self.driver =driver;
        self.locator = None;
        self.element = None;
        self.action ="";


    def find_elements(self,locator,action="",**kwargs):
        try:
            self.wait_time(2);
            return self.driver.find_elements(*locator);
        except Exception as e:
            self.log.exception("{}功能,在页面查找多个元素{}失败".format(self.name,locator));
            raise e;



    def wait_element_is_visiable(self,locator,action="",**kwargs):
        """
            查找等待元素可见
            :param locator:
            :param action:
            :param kwargs:
            :return:
        """
        try:
            self.locator=locator;
            self.action=action;
            # 没有设置默认时间的话，就读取默认时间
            timeout = kwargs.get("timeout",setting.DEFAULT_TIMEOUT);
            poll_frequency = kwargs.get("poll_frequency",0.5);
            self.element = WebDriverWait(driver=self.driver,timeout=timeout,poll_frequency=poll_frequency).until(
                    EC.visibility_of_element_located(locator=locator)
                )
        except Exception as e:
            self.log.exception("在{}，进行{}操作，等待{}元素可见失败".format(self.name,self.action,self.locator));
            self.get_page_screehot(action=action);
            raise e;
        else:
            self.log.info("在{}，进行{}操作，等待{}元素可见成功".format(self.name
    ,self.action,self.locator));
            return self;




    def wait_element_to_be_clicked(self,locator,action="",**kwargs):
        """
        等待元素可以被点击
        :param locator:
        :param action:
        :param kwargs:
        :return:
        """
        try:
            self.action=action;
            self.locator=locator;
            timeout= kwargs.get("timeout",self.setting.DEFAULT_TIMEOUT);
            poll_frequency= kwargs.get("poll_frequency",0.5);
            self.element =WebDriverWait(driver=self.driver,timeout=timeout,poll_frequency=poll_frequency)\
                .until(EC.element_to_be_clickable(locator=locator));
        except Exception as e:
            self.log.exception("在{},进行{}操作，等待元素{}可以被点击失败".format(self.name,self.action,self.locator))
            self.get_page_screehot(action=action);
            raise e;
        else:
            self.log.info("在{},进行{}操作,等待元素{}可以被点击成功".format(self.name,self.action,self.locator));
            return self;



    def wait_element_presence_located(self,locator,action,**kwargs):
        """
        等待元素出现
        :param locator:
        :param action:
        :param kwargs:
        :return:
        """
        try:
            self.locator = locator;
            self.action=action;
            timeout=kwargs.get("timeout",self.setting.DEFAULT_TIMEOUT);
            poll_frequency= kwargs.get("poll_frequency",0.5);
            self.element = WebDriverWait(driver=self.driver,timeout=timeout,poll_frequency=poll_frequency)\
                .until(EC.presence_of_element_located(locator));
        except Exception as e:
            self.log.exception("在{},进行{}操作,等待{}元素出现【失败】".format(self.name,self.action,self.locator))
            self.get_page_screehot(action=self.action);
            raise e;
        else:
            self.log.info("在{},进行{}操作,等待{}元素出现【成功】".format(self.name,self.action,self.locator))
            return self;




    def get_element(self):
        """
        获取元素
        :return:
        """
        if self.element is None:
            raise RuntimeError("不在可以在调用wait方法之前，调用此方法");
        return self.element;



    def click_element(self):
        """
        点击元素
        :return:
        """
        if self.element is None:
            raise RuntimeError("不可以在调用wait方法之前,调用此方法");

        try:
            self.element.click();
        except Exception as e:
            self.log.exception("在{},{}操作的时候，点击元素{}失败".format(self.name,self.action,self.locator));
            self.get_page_screehot(action=self.action);
            raise e;
        else:
            self.log.info("在{},进行{}操作的时候,点击元素{}成功".format(self.name,self.action,self.locator));
        finally:
            # 清空缓存
            self.__clea_cache();


    def send_keys(self,content):
        """
        输入框输入内容
        :param content:
        :return:
        """
        if self.element is None:
            raise RuntimeError("不可以在调用wait方法之前调用该方法");

        try:
            self.element.clear();
            self.element.send_keys(content);
        except Exception as e:
            self.log.exception("在{},进行{}操作的时候,对元素{}输入{},【失败】".format(self.name,self.action,self.locator,content));
            self.get_page_screehot(action=self.action);
            raise e;
        else:
            self.log.info("在{},进行{}操作的时候,对元素{}输入{},【成功】".format(self.name,self.action,self.locator,content));
        finally:
                self.__clea_cache();

    def  get_element_text(self):
        """
        获取元素文本内容
        :return:
        """
        if self.element is None:
            raise RuntimeError("不可以在调用wait方法之前调用该方法");
        try:
            text = self.element.text;
        except Exception as e:
            self.log.exception("在{} 进行{}操作获取元素{}文本内容【失败】".format(self.name,self.action,self.locator));
            self.get_page_screehot(action=self.action);
            raise e;
        else:
            self.log.info("在{},进行>>{}<<操作获取元素{}文本内容【成功】,文本内容是:{}".format(self.name,self.action,self.locator,text));
            return text;


    def get_element_attr(self,name):
        """
        获取元素属性的值
        :param name:
        :return:
        """
        if self.element is None:
            raise  RuntimeError("不可以在调用wait方法之前调用此方法");
        try:
            value = self.element.get_attribute(name=name);
        except Exception as e:
            self.log.exception("在{},进行{}操作获取元素{}属性的值【失败】".format(self.name,self.action,self.locator));
            self.get_page_screehot(action=self.action);
            raise e;
        else:
            self.log.info("在{},进行{}操作获取元素{}属性的值【成功】，属性的值是:{}".format(self.name,self.action,self.locator,value));
            return name;


    def switch_to_new_windows(self,handle=None,action=''):
        """
        切换窗口
        :param handle:
        :param action:
        :return:
        """
        try:
            if handle:
                self.driver.switch_to.window(handle);
            else:
                #获取当前窗口
                original_window = self.driver.current_window_handle
                for handle in self.driver.window_handles:
                    if handle != original_window:
                        self.driver.switch_to.window(handle);
                        break;
        except Exception as e:
            self.log.exception("在{},{}操作的时候，切换到窗口{}【失败】".format(self.name,action,handle));
            self.get_page_screehot(action=action);
            raise e;
        else:
            self.log.info("在{},{}操作的时候，切换到窗口{}【成功】".format(self.name,action,handle));




    def wait_time(self,time=1):
        """
        等待时间
        :param time:
        :return:
        """
        sleep(time);
        return self;



    def get_page_screehot(self,action):
        # 错误截图报错路径
        img_path = os.path.join(setting.ERROR_SCREENSHOT_DIR,"{}_{}操作 {}.png".format(
            self.name,action,datetime.datetime.strftime("%Y-%m-%d %H-%M-%S")));

        if self.driver.save_screenshot(img_path):
            self.log.info("生成错误截图:{}【成功】".format(img_path));
        else:
            self.log.error("生成错误截图:{},【失败】".format(img_path));

    def table_cell(self,tr=1,td=1):
         """
            获取biaod
        :param tr:
        :param td:
        :return:
         """
         locator = "//table//tr[{}]/td[{}]//span//span".format(tr,td);
         self.wait_element_presence_located(locator=locator,action="定位选择框");


    def switch_alert_action(self,action="接受"):
        try:
            alter = self.driver.switch_to.alter;
            if action=="接受":
                alter.accept();
                self.log.info("在{},{}操作是切换到弹出款并且点击确定成功");
            else:
                alter.dismiss();
                self.log.info("在{},{}操作是切换到弹出款并且点击取消成功");
        except Exception as e:
            self.log.exception("在{},{}操作的时候，切换到弹出框的时候【失败】".format(self.name, action));
            self.get_page_screehot(action=action);
            raise e;


    def select_elemet(self,**kwargs):
        try:
            self.log.info("111111{}".format(kwargs));
            list_1 =["index","text","value"]
            for i in kwargs.keys():
                if i not in list_1:
                    raise RuntimeError("此方法必须包含:{}其中一个参数".format(list_1));
            if kwargs.get("index").isdigit():
                Select(self.element).select_by_index(int(kwargs.get("index")));
            elif kwargs.get("text","") != "":
                Select(self.element).select_by_visible_text(kwargs["text"]);
            elif kwargs.get(["value"],"") != "":
                Select(self.element).select_by_value(kwargs["value"]);
            self.log.info("在{},{}操作,选择元素成功".format(self.name,self.action));
        except Exception as e:
            self.log.info("在{},{}操作,选择元素失败".format(self.name,self.action));
            self.get_page_screehot(action=self.action);
            raise e;

    def switch_to_new_iframe(self):
            pass;


    def __clea_cache(self):
        """
        清楚缓存
        :return:
        """

        self.element=None;
        self.action="";
        self.locator=None;