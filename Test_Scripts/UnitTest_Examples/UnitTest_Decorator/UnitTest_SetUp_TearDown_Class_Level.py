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

    def test_login_to_orangeHRM(self):
        username = self.driver.find_element(By.NAME, 'txtUsername')
        password = self.driver.find_element(By.NAME, 'txtPassword')
        LoginButton = self.driver.find_element_by_id('btnLogin')
        username.send_keys("Admin")
        password.send_keys("admin123")
        LoginButton.click()

    def test_logout_from_orangeHRM(self):
        self.driver.find_element(By.ID, 'welcome').click()
        self.driver.implicitly_wait(2)  # seconds
        self.driver.find_element(By.LINK_TEXT, 'Logout').click()
        self.driver.implicitly_wait(5)  # seconds
        self.driver.find_element_by_id('logInPanelHeading').is_displayed()

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

    if __name__ == '__main__':
        unittest.main()
