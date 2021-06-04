import unittest
import sys
import time
import unittest
from typing import List

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


class CompareTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a new Chrome session
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        # Target URL
        cls.driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")
        cls.driver.maximize_window()

    def test1_login_to_orangeHRM(self):
        username = self.driver.find_element(By.NAME, 'txtUsername')
        password = self.driver.find_element(By.NAME, 'txtPassword')
        LoginButton = self.driver.find_element_by_id('btnLogin')
        username.send_keys("Admin")
        password.send_keys("admin123")
        LoginButton.click()

    def test2_Click_Admin(self):
        Admin = self.driver.find_element_by_link_text("Admin").click()

    def test3_Compare_DD_Values(self):
        status_dd = Select(self.driver.find_element_by_id("searchSystemUser_status"))
        status_values = status_dd.options

        list1 = []
        for i in range(len(status_values)):
            list = status_values[i].text
            list1.append(list)
            print(list1)
        self.assertListEqual(list1, ['All', 'Enabled', 'Disabled'], 'List values Matched')






        #self.assertListEqual([1, 2, 3, 4,5], [1, 2, 3, 4,5])



if __name__ == '__main__':
    unittest.main()
