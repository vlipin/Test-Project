#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
from base_object import BaseObject


class FindMeetingPage(BaseObject):
    """@description: class with element getters and action methods for Find a Meeting page
           @author: vlipinskyy"""

    def __init__(self):
        super(FindMeetingPage, self).__init__()
        self.wait = WebDriverWait(self.driver, self._test_timeout)

    def get_meeting_search_textfield(self):
        return self.get_element_by_id("meetingSearch")

    def get_first_result_title(self):
        return self.get_element_by_css(
            "div#ml-1180510>result-location>div>div>a>location-address>div>div>div>div>span")

    def get_first_result_distance(self):
        return self.get_element_by_css(
            "div#ml-1180510>result-location>div>div>a>location-address>div>div>div>div.location__distance")

    def get_todays_hours_text(self):
        return self.get_element_by_class("hours-list--currentday").text

    def get_first_result_title_after_click(self):
        return self.get_element_by_class("location__name").text

    def type_meeting_search_textfield(self, search_term):
        self.get_meeting_search_textfield().send_keys(search_term)

    def get_first_result_title_text(self):
        return self.get_first_result_title().text

    def get_first_result_distance_text(self):
        return self.get_first_result_distance().text

    def click_first_result(self):
        self.get_first_result_title().click()