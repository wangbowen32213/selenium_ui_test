#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys

sys.path.append('.')
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from config.conf import LOCATE_MODE
from tools.times import sleep
import os
from tools.logger import log
import win32.lib.win32con as win32con
import win32.lib.win32gui_struct as win32gui_struct
"""
selenium基类
本文件存放了selenium基类的封装方法
"""

class WebPage(object):
    """selenium 基类，存放selenium基类的封装方法"""

    def __init__(self,driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.timeout = 20
        self.wait = WebDriverWait(self.driver,self.timeout)

    def get_url(self,url):
        # self.driver.maximize_window()
        self.driver.set_page_load_timeout(60)
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            log.info("打开网页：%s" % url)
        except TimeoutException:
            raise TimeoutException("打开%s超时，请检查网络或网络服务器" % url)

    def find_element(self,locator):
        """查找元素"""
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )


    def find_elements(self,locator):
        """查找多个元素，返回元素列表"""
        return self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )

    def elements_num(self,locator):
        """获取相同元素的个数"""
        number = len(self.find_elements(locator))
        log.info("相同元素：{}".format((locator,number)))
        return number

    def input_text(self,locator,txt):
        """在指定元素处输入字符串"""
        el = self.find_element(locator)
        el.clear()
        el.send_keys(txt)
        log.info("输入文本：{}".format(txt))


    def click_action(self,locator):
        """点击元素"""
        self.find_element(locator).click()
        sleep(0.5)
        log.info("点击元素：{}".format(locator))

    def element_text(self,locator):
        """返回指定元素的文本信息"""
        _text = self.find_element(locator).text
        log.info("获取文本：{}".format(_text))
        return _text

    @property
    def get_source(self):
        """获取页面源代码"""
        return self.driver.page_source

    def refresh(self):
        """刷新页面F5"""
        self.driver.refresh()
        self.driver.implicitly_wait(30)

    def script(self,src):
        """执行js"""
        return  self.driver.execute_script(src)

    def update_file(self,path_file,title="文件上传",type_class='#32770',calssnameNN_searh='Edit',calssnameNN_button='Button'):
        """
        文件上传，默认为火狐浏览器
        :param path_file: 需要上传的文件路径
        :param title: 上传弹框的title
        :param type_class: class_id
        :param calssnameNN_searh: 搜索栏的classname
        :param calssnameNN_button: 打开按钮的classname
        :return:
        """
        dialog = win32gui_struct.win32gui.FindWindow(type_class, title)  # 对话框
        ComboBoxEx32 = win32gui_struct.win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui_struct.win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui_struct.win32gui.FindWindowEx(ComboBox, 0, calssnameNN_searh, None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        button = win32gui_struct.win32gui.FindWindowEx(dialog, 0, calssnameNN_button, None)  # 确定按钮Button

        # win32gui_struct.win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None,'C:\\Users\\cao\\Desktop\\5.jpg')  # 往输入框输入绝对地址
        win32gui_struct.win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None,path_file)  # 往输入框输入绝对地址
        win32gui_struct.win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button

    def updata_file_autolt(self,exe_path,file_path):
        """
        使用autolt生成的exe上传文件
        :param exe_path:exe文件路径
        :param file_path:上传文件路径
        :return:
        """
        os.system(r'%s "%s"' % (exe_path,file_path))




if __name__ == '__main__':
    driver = webdriver.Firefox()
    aa = WebPage(driver)
    aa.get_url("https://www.baidu.com/")
    bb = aa.find_element((By.CSS_SELECTOR,"#kw"))
    bb.send_keys("123")

    driver.find_element()





