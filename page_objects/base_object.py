#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import NoSuchElementException, WebDriverWait
from code_base.webdriver_factory import WebdriverFactory
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class BaseObject(object):
    """@description: class with overwritten WebDriver functions and additional features to handle page elements
       @author: vlipinskyy"""

    BROWSER = "mac_chrome"


    def __init__(self):
        self.driver = WebdriverFactory().get_driver(self.BROWSER)
        self.actions = ActionChains(self.driver)
        self._test_timeout = 10

    def get_element_by_class(self, elem_class, timeout = 10):
        """Function to wait until element is located on the page and then return it using CSS
           :param
                    css - unique css selector
                    timeout - time in .ms to wait until element become visible. Exception raises after stated time is over.
           :return WebElement
        """
        try:
            WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located((By.CLASS_NAME, elem_class)))
        except:
            # Raising exeption of No needed element is found
            NoSuchElementException("Element is not found by CLASS on the page after timeout of" + str(timeout))

        return self.driver.find_element_by_class_name(elem_class)

    def get_element_by_id(self, id, timeout = 10):
        """Function to wait until element is located on the page and then return it using ID
           :param
                    id - unique id selector
                    timeout - time in .ms to wait until element become visible. Exception raises after stated time is over.
           :return WebElement
        """
        try:
            WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located((By.ID, id)))
        except:
            # Raising exeption of No needed element is found
            NoSuchElementException("Element is not found by ID on the page after timeout of" + str(timeout))

        return self.driver.find_element_by_id(id)

    def get_element_by_css(self, css, timeout = 10):
        """Function to wait until element is located on the page and then return it using CSS
           :param
                    css - unique css selector
                    timeout - time in .ms to wait until element become visible. Exception raises after stated time is over.
           :return WebElement
        """
        try:
            WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located((By.CSS_SELECTOR, css)))
        except:
            # Raising exeption of No needed element is found
            NoSuchElementException("Element is not found by CLASS on the page after timeout of" + str(timeout))

        return self.driver.find_element_by_css_selector(css)

    def go_to_target_page(self, url):
        """Function to get the target page by URL
           :param
                    url - exact url of the page
        """
        self.driver.get(url)

    def get_title(self):
        """Function to get the target page by URL
                :return title of page in String
        """
        return self.driver.title

    def click_enter_button(self):
        """Function to click ENTER button using ActionChains of Selenium"""
        self.actions.send_keys(Keys.ENTER)
        self.actions.perform()