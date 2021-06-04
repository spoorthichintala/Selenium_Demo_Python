import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
class OrangeHRM_Login_Logout(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # Target URL
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        time.sleep(5)
    def test_02_login_to_orangeHRM(self):
        Act_Text = self.driver.title
        print(Act_Text)
        Exp_Text = Act_Text
        # assertIs() to check that if first & second evaluated to same object
        self.assertIs(Exp_Text,Act_Text,"Title not displayed")
        self.driver.find_element_by_name('txtUsername').send_keys("Admin")
        self.driver.find_element_by_name('txtPassword').send_keys("admin123")
        self.driver.find_element_by_id('btnLogin').click()
        act_url = self.driver.current_url
        self.assertNotEqual("https://opensource-demo.orangehrmlive.com/index.php/auth/login", act_url,"Both value are not equal")
        time.sleep(5)
    @classmethod
    def tearDownClass(self):
        # close the browser window
        self.driver.quit()
    if __name__ == '__main__':
        unittest.main()
