#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from selenium import webdriver
import threading


class WebdriverFactory():
    """@description: Factory class to create a unique instance of Web Driver
       @author: vlipinskyy"""

    # Dictionary to fill with all created WebDriver instances
    DRIVERS = dict()

    def create_driver(self, key, browser):
        """Function to create a WebDriver instance and pop it to the DRIVER dict
           :param
                    key - number of thread running with single selenium web driver instance for each
                    browser - type of browser and env (remote or local) we need to run. 1 remote and 3 local options for now:
                            chrome_remote ; ff , chrome and ie. this param is set in config.ini
           :return WebDriver
        """
        if browser == "ff":
            # Create a new instance of the Firefox driver
            self.driver = webdriver.Firefox()
        elif browser == "mac_chrome":
            # Create a new instance of the Chrome driver for Mac
            self.driver = webdriver.Chrome("./chromedrivers/mac_chromedriver/chromedriver")
        elif browser == "linux_chrome":
            # Create a new instance of the Chrome driver for Linux
            self.driver = webdriver.Chrome("./chromedrivers/linux_chromedriver/chromedriver")
        else:
            # Browser is not recognized
            raise NameError('Browser name is not recognized, exiting...')
        # Set new created WebDriver to DRIVERS dictionary
        self.DRIVERS[key] = self.driver

        return self.driver

    def get_driver(self, browser):
        """Function to call or create only one instance of WebDriver (to open just one instance of browser for each test)
           :param
                    browser - type of browser and env (remote or local) we need to run. 1 remote and 3 local options for now:
                            chrome_remote ; ff , chrome and ie. this param is set in config.ini
           :return WebDriver
        """
        #Getting a key for the currnet thread running
        key = threading.currentThread().getName()

        if self.DRIVERS.get(key) is None:
            # Returning a Driver if it does not exist
            return self.create_driver(key, browser)
        else:
            # Creating and returning a Driver if it exists
            return self.DRIVERS.get(key)

    def quit_driver(self):
        """Function to quite a driver. Raising exeption if current thread is empty."""

        # Getting a key for the currnet thread running
        key = threading.currentThread().getName()

        if self.DRIVERS.get(key) is not None:
            #Check if WebDriver exists and close it, remove the key
            self.DRIVERS.get(key).quit()
            self.DRIVERS.pop(key)
        else:
            # Raising exeption of non existing driver
            raise Exception("Attempt to quite non existing driver. Tread - " + key)