#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
from selenium.webdriver.common.by import By
from selenium import webdriver
from config.conf import FIREFOX_UPDATE_FILE
from config.conf import UPDATE_FILE
sys.path.append('.')

from page.webpage import WebPage, sleep

class SearchPage(WebPage):
    """页面类型，每个页面一个文件"""

    search_input = (By.CSS_SELECTOR,"#kw")
    #输入框按钮
    search_picture_button = (By.CSS_SELECTOR,".soutu-btn")
    #输入框按图片搜索按钮
    file_update_button = (By.CSS_SELECTOR,".upload-wrap>input")
    #选择文件按钮
    file_update_button2 = (By.CSS_SELECTOR,".upload-wrap")
    #选择文件按钮
    search_button = (By.CSS_SELECTOR,"#su")
    #搜索按钮

    def input_srarch_str(self,str):
        """向输入框输入字符串"""
        self.input_text(self.search_input,str)
        sleep(1)

    def update_file_pacther(self,path):
        """向输入框输入字符串"""
        self.input_text(self.file_update_button,path)

    def click_search(self):
        """点击百度一下按钮"""
        self.click_action(self.search_button)
        sleep(1)

    def click_search_picture_button(self):
        """点击图片搜索按钮"""
        self.click_action(self.search_picture_button)

    def click_file_update_button(self):
        """点击图片选择按钮"""
        self.click_action(self.file_update_button2)

if __name__ == '__main__':
    driver = webdriver.Firefox()
    aa = SearchPage(driver)
    aa.get_url("https://www.baidu.com/")
    aa.click_search_picture_button()
    # aa.update_file_pacther(UPDATE_FILE)
    aa.click_file_update_button()
    sleep(1)
    print("1111111111111")
    aa.updata_file_autolt(FIREFOX_UPDATE_FILE,UPDATE_FILE)