#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys

sys.path.append('.')

import os

from selenium.webdriver.common.by import By
#获取项目目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#配置文件路径
INI_PATH = os.path.join(BASE_DIR,'config','config.ini')

# 页面元素目录
ELEMENT_PATH = os.path.join(BASE_DIR, 'page_element')

# 日志目录
LOG_PATH = os.path.join(BASE_DIR, 'logs')

# 报告目录
REPORT_PATH = os.path.join(BASE_DIR, 'report', 'report.html')

# allure报告目录
ALLURE_REPORT = os.path.join(BASE_DIR, 'allure-report')

# allure原始数据
ALLURE_RESULTS = os.path.join(BASE_DIR, 'allure-results')

# 截图目录
SCREENSHOT_DIR = os.path.join(BASE_DIR, 'screen_capture')

# 上传文件exe文件,火狐可用
FIREFOX_UPDATE_FILE = os.path.join(BASE_DIR, 'package',"firefox_update.exe")

# 测试文件
UPDATE_FILE = os.path.join(BASE_DIR, 'package',"test.png")


# 元素定位的类型
LOCATE_MODE = {
    'css': By.CSS_SELECTOR,
    'xpath': By.XPATH,
    'name': By.NAME,
    'id': By.ID,
    'class': By.CLASS_NAME
}

# 邮件信息
EMAIL_INFO = {
    'username': 'test@163.com',
    # 切换成你自己的地址
    'password': '',
    #邮箱授权码
    'smtp_host': 'smtp.163.com',
    'smtp_port': 465
}

# 收件人
ADDRESSEE = [
    'wbw19930822@163.com',
]

MYSQL_INFO={
    "hosts" : "127.0.0.1",
    # hosts = "localhost"
    #地址
    "port" : 3306,
    #端口
    "username" : "root",
    #用户名
    "password" : "123456",
    #密码
    "db_name" : "user_admin"
    #数据库名称
}


#依赖文件路径
PACKAGE_FILE = os.path.join(BASE_DIR,'package')




if __name__ == '__main__':
    # print(INI_PATH)
    print(EMAIL_INFO['smtp_host'])
    # print(ADDRESSEE[-1])