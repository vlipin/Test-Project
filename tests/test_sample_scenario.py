#!/usr/bin/env python
# -*- encoding: utf-8 -*-


import datetime
from nose.plugins.attrib import attr
from nose.tools import assert_equal
from nose.tools import assert_true
from nose.tools import istest

from base_test import BaseTest
from page_objects.login_page_object import LoginPage
from  page_objects.find_meeting_page_object import FindMeetingPage


class SampleTest(BaseTest):
    """Class for implementing sample scenarios for WW site"""

    def setUp(self):
        super(SampleTest, self).setUp()
        self.login_page = LoginPage()
        self.find_meeting_page = FindMeetingPage()

    @istest
    @attr(type='REGRESSION')
    def test_sample_workflow(self):
        """Test Function to test given flow and cover necessary parts of WW site"""

        #Local variables
        expected_login_page_title = "Weight Loss Program, Recipes & Help | WW America"
        expected_find_meeting_title = "Get Schedules & Times Near You"

        actual_login_page_title = self.login_page.get_title()
        # Asserting the title on Login page
        assert_true(expected_login_page_title in actual_login_page_title,
                    "Actual title at 'Login' page should contains expected string: no {0} in {1}".format(
                                                                    expected_login_page_title, actual_login_page_title))

        # Redirect user to 'Find a Meeting' page
        self.login_page.click_find_a_meeting_btn()
        actual_find_meeting_title = self.find_meeting_page.get_title()
        # Asserting the title on 'Find a Meeting' page
        assert_true(expected_find_meeting_title in actual_find_meeting_title,
                    "Actual title at 'Find a Meeting' page should contains expected string: no {0} in {1}".format(
                        expected_find_meeting_title, actual_find_meeting_title))

        # Input into Search textfield and hit Enter emulation
        self.find_meeting_page.type_meeting_search_textfield("10011")
        self.find_meeting_page.click_enter_button()

        location_name_before_click = self.find_meeting_page.get_first_result_title_text()
        # Output of 1st search result Name and Location
        print "First result title: {0}".format(location_name_before_click)
        print "First result distance: {0}".format(self.find_meeting_page.get_first_result_distance_text())

        # Click at first Result
        self.find_meeting_page.click_first_result()

        location_name_after_click = self.find_meeting_page.get_first_result_title_after_click()

        # Asserting the name of 1st result location before and after click
        assert_equal(location_name_before_click, location_name_after_click,
                    "Location names before and after click should be the same: no {0} in {1}".format(
                        location_name_before_click, location_name_after_click))

        # Output Todays hours of operation
        full_time_info = self.find_meeting_page.get_todays_hours_text()
        print full_time_info[8:]