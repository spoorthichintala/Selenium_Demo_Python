import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


class OrangeHRM_Login_Logout(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create a new Chrome session
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        # Target URL
        cls.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        time.sleep(10)
    def test_02_login_to_orangeHRM(self):
        self.driver.find_element_by_name('txtUsername').send_keys("Admin")
        self.driver.find_element_by_name('txtPassword').send_keys("admin123")
        self.driver.find_element_by_id('btnLogin').click()

        act_url = self.driver.current_url
        self.assertNotEqual("https://opensource-demo.orangehrmlive.com/index.php/auth/login", act_url,"Both value are not equal")
        time.sleep(8)
        link_text = self.driver.find_element_by_link_text("Dashboard").text
        print(link_text)

    def test_03_extract_status_values(self):
        time.sleep(3)
        Admin_menu = self.driver.find_element_by_xpath("//b[normalize-space()='Admin']")
        action = ActionChains(self.driver)
        action.move_to_element(Admin_menu).perform()
        user_mgmt = self.driver.find_element_by_xpath("//a[normalize-space()='User Management']")
        action.move_to_element(user_mgmt).perform()
        users = self.driver.find_element_by_xpath("//a[normalize-space()='Users']")
        action.move_to_element(users).perform()
        users.click()
        time.sleep(5)
        status = Select(self.driver.find_element_by_id("searchSystemUser_status"))
        status_values = status.options
        list1 =[]
        for index in range(len(status_values)):
            list = status_values[index].text
            list1.append(list)
        print(list1)
        self.assertListEqual(list1,['All','Enabled','Disabled'],'List values Matched')



    def test_04_logout_from_orangeHRM(self):
        self.driver.find_element(By.ID, 'welcome').click()
        self.driver.implicitly_wait(2)  # seconds
        self.driver.find_element(By.LINK_TEXT, 'Logout').click()
        self.driver.implicitly_wait(5)  # seconds
        self.driver.find_element_by_id('logInPanelHeading').is_displayed()
        Act_Text = self.driver.find_element_by_id('logInPanelHeading').text
        print(Act_Text)
        Exp_Text = "LOGIN Panel"
        self.assertEqual(Act_Text,"LOGIN Panel")
        self.assertTrue(Act_Text=="LOGIN Panel")
        # self.assertIs(Exp_Text,Act_Text,"Login Panel text not displayed")
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

    if __name__ == '__main__':
        unittest.main()
