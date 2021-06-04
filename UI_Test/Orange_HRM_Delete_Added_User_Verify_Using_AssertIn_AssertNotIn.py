import random
import time
import unittest
import self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

class Verify_User(unittest.TestCase):
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

    def test2_Verify_dashboard(self):
     self.driver.find_element_by_link_text('Dashboard').is_displayed()

    def test3_Verify_Useradded(self):
    #Click on Admin
     self.driver.find_element_by_link_text('Admin').click()
    # Click on Add Button
     self.driver.find_element_by_name('btnAdd').click()

    #Select Admin from Dropdown Value
     dropdown= Select(self.driver.find_element_by_id('systemUser_userType'))
     dropdown.select_by_visible_text('Admin')

     self.driver.find_element_by_id("systemUser_employeeName_empName").send_keys("Fiona Grace")
     randomInt = random.randint(0,1000)
     self.driver.find_element_by_id("systemUser_userName").send_keys("abhi" + str(randomInt))

    #ExpUserName = browser.find_element_by_id("systemUser_userName").text
     self.driver.find_element_by_id("systemUser_password").send_keys("admin123")
     self.driver.find_element_by_id("systemUser_confirmPassword").send_keys("admin123")
     time.sleep(5)
     self.driver.find_element_by_id("btnSave").click()
     time.sleep(5)



    def test4_Verify_deleted(self):

        #self.driver.find_element_by_xpath("//td/a[text()='" + ExpUserName + "']//parent::td/../td/input").click()
        #cellvalue = self.driver.find_element_by_xpath("//a[text()='" + ExpUserName + "']")
        ExpUserName = "abhi" + str(randomInt)
        self.driver.refresh()
        cellvalue=self.driver.find_element_by_xpath("//td/a[text()='" + ExpUserName + "']//parent::td/../td/input").click()
        textvalue = cellvalue.text
        self.assertIn(ExpUserName, textvalue, "User is present in the lits")
        time.sleep(5)
        self.driver.find_element_by_id("btnDelete").click()
        self.driver.find_element_by_id("dialogDeleteBtn").click()
        self.assertNotin(self.ExpUserName,textvalue,"User is not present in the lits")
        time.sleep(5)
        self.driver.close()
if __name__=='__main__':
    unittest.main()


#//a[text()='"+ ExpUserName +"']


#print(textvalue)
#assert ExpUserName == textvalue
time.sleep(10)


#Delete Added user from WebTable

#browser.find_element_by_xpath("//a[text()='"+ExpUserName+"']/parent::td/preceding-sibling::td/input").click()
