#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import unittest
from code_base.webdriver_factory import WebdriverFactory
from page_objects.base_object import BaseObject


class BaseTest(unittest.TestCase):
    """@description: class to provide SetUp and TearDown as well as global vars and method declarations
               @author: vlipinskyy"""

    APP_BASE_URL = "https://www.weightwatchers.com/us/"

    def setUp(self):
        self.base_object = BaseObject()
        self.base_object.go_to_target_page(self.APP_BASE_URL)

    def tearDown(self):
        try:
            WebdriverFactory().quit_driver()
        except:
            pass

    if __name__ == '__main__':
        unittest.main(verbosity=2)