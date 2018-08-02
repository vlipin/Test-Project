#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
from base_object import BaseObject


class LoginPage(BaseObject):
    """@description: class with element getters and action methods for Login page
               @author: vlipinskyy"""
    def __init__(self):
        super(LoginPage, self).__init__()
        self.wait = WebDriverWait(self.driver, self._test_timeout)

    def get_find_a_meeting_btn(self):
        return self.get_element_by_class("find-a-meeting")

    def click_find_a_meeting_btn(self):
        self.get_find_a_meeting_btn().click()