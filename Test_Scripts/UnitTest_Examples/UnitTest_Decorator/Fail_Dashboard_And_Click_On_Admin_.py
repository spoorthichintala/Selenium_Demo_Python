import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class OrangeHRM_Login_Logout(unittest.TestCase):
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

    def test2_verify_Dashboard(self):
        time.sleep(5)
        Dashboard_text = self.driver.find_element_by_link_text("Dashboard1").text
        print(Dashboard_text)
        assert Dashboard_text == "Dashboard"

    def test3_Click_Admin(self):
        time.sleep(2)
        Admin =self.driver.find_element_by_link_text('Admin').click()

    def test4_logout_from_orangeHRM(self):
        self.driver.find_element(By.ID, 'welcome').click()
        self.driver.implicitly_wait(2)  # seconds
        self.driver.find_element(By.LINK_TEXT, 'Logout').click()
        time.sleep(5)
        self.driver.find_element_by_id('logInPanelHeading').is_displayed()

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

if __name__ == '__main__':
        #Use failfast concept, so that if any test fail, it will come out rather than executing
        # remaining method
        unittest.main(failfast=True)
