#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/10/19  下午11:52
# @Author  : yantianpeng
# @Site    : 
# @File    : aa.py
# @Software: PyCharm
'''
from selenium import webdriver;
from selenium.webdriver.common.by import By
from time import sleep
import setting
try:
    wd = webdriver.Chrome(executable_path="/Users/yantianpeng/Downloads/chromedriver")
    wd.maximize_window()

    wd.get(setting.PROJECT_HOST_VUE)
    sleep(5)
    wd.find_element_by_xpath("//input[@name='username']").send_keys("admin");
    wd.find_element_by_xpath("//input[@name='password']").send_keys("admin");
    wd.find_element_by_xpath("//span[text()='登录']").click();
    sleep(2);  # '//span[text()="系统设置"]'
    wd.find_element_by_xpath('//span[text()="系统设置"]').click();
    sleep(2);
    wd.find_element_by_xpath("//span[text()='用户管理']").click();



    #点击添加
    sleep(3)
    wd.find_element_by_xpath("//button[@type='button']//span[contains(text(),'添加')]").click();
    sleep(2);
    #
    # #点击角色选择
    # wd.find_element_by_xpath('//input[@placeholder="请选择角色"]/following-sibling::span//i').click();
    # sleep(2)
    # wd.find_element_by_xpath("//span[text()='student']").click();
    # sleep(3)
    # wd.find_element_by_xpath("//label[text()='姓名']/following-sibling::div//input").click();
    # #输入姓名
    # wd.find_element_by_xpath("//label[text()='姓名']/following-sibling::div//input").send_keys("as")
    # wd.find_element_by_xpath("//label[text()='用户名']/following-sibling::div//input").send_keys("ss");
    #
    # # 选择部门
    wd.find_element_by_xpath("//label[text()='部门']/following-sibling::div//input").click();
    # wd.find_element_by_xpath("//label[text()='部门']/following-sibling::div//input").send_keys("sasa")
    sleep(3);
    element = wd.find_elements(By.XPATH,"//span[@class='el-tree-node__label']")
    element[0].click();

    #wd.find_element_by_xpath("//span[contains(text(),'确 定')]/parent::button").click();
    # wd.find_element_by_xpath('//th[@colspan="1"]//div[text()="用户名"]/preceding::th//span//span').click();
    # sleep(2);
    # wd.find_element_by_xpath('//input[contains(@placeholder,"已选")]').click();
    # sleep(5);
    # wd.find_element_by_xpath('//span[text()="删除"]').click();

except Exception as e:
    print("---{}".format(e));
finally:
    sleep(9)
    wd.quit();