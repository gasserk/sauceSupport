#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
import time
from selenium import webdriver

class Selenium2OnSauce(unittest.TestCase):

    def setUp(self):
        self.desired_capabilities = webdriver.DesiredCapabilities.CHROME
        self.desired_capabilities['version'] = '34'
        self.desired_capabilities['platform'] = 'OS X 10.9'
        self.desired_capabilities['name'] = 'Editing the DNS'
        self.desired_capabilities['prerun'] = {'executable':'https://raw.githubusercontent.com/albedithdiaz/sauceSupport/master/EditDNS.sh', 'background': False }
        
        self.driver = webdriver.Remote(command_executor = 'http://SAUCE_USERNAME:SAUCE_ACCESS_KEY@ondemand.saucelabs.com:80/wd/hub', desired_capabilities = self.desired_capabilities)
        self.driver.implicitly_wait(30)    

    def test_sauce(self):
        self.driver.get('http://www.saucelabs.com')
        title = self.driver.title
        self.assertEquals("Google", title)  

    def tearDown(self):
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()
