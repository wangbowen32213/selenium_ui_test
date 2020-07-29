#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')

import re
import pytest
import allure
from tools.logger import log
from common.readconfig import ini
from page_object.searchpage import SearchPage
# from selenium import webdriver

@allure.feature("测试百度模块")
class TestSearch:
    @pytest.fixture(scope='function', autouse=True)
    def open_baidu(self,drivers):
        """打开网站"""
        # driver = webdriver.Firefox()
        search = SearchPage(drivers)
        search.get_url(ini.url)

    @allure.story("搜索selenium结果用例")
    def test_001(self,drivers):
        """搜索"""
        search = SearchPage(drivers)
        search.input_srarch_str("selenium")
        search.click_search()
        result = re.search(r'selenium', search.get_source)
        log.info(result)
        assert result

    @allure.story("测试搜索候选用例")
    def test_002(self,drivers):
        """搜索"""
        search = SearchPage(drivers)
        search.input_srarch_str("selenium")
        search.click_search()
        result = re.search(r'12213123123', search.get_source)
        log.info(result)
        assert result

    @allure.story("测试搜索候选用例")
    def test_003(self,drivers):
        """搜索"""
        search = SearchPage(drivers)
        search.input_srarch_str("测试")
        search.click_search()
        result = re.search(r'12213123123', search.get_source)
        log.info(result)
        assert result


if __name__ == '__main__':
    pytest.main(['TestCase/test_search.py'])
