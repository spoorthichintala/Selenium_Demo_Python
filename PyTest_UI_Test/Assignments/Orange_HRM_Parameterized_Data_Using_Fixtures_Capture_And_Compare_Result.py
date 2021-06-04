import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("driver_init","app_url")
class BasicTest:
    pass


@pytest.mark.parametrize("uname, upass,Exp_result", [("Admin", "admin123","Dashboard"),("Admin1", "admin123","Invalid credentials"),("", "admin123","Username cannot be empty"),("Admin", "admin1234","Invalid credentials"),("Admin", "","Password cannot be empty")])
class Test_OrangeHRM_Login(BasicTest):

     def test_open_url(self, uname, upass,Exp_result,app_url):
        # Step 2) Navigate to OrangeHRM
        #self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.get(app_url)
        # Step 3) Enter the Username & Enter Password
        username = self.driver.find_element_by_name("txtUsername")
        password = self.driver.find_element_by_name("txtPassword")
        submit = self.driver.find_element_by_name("Submit")
        username.send_keys(uname)
        password.send_keys(upass)
        # Step 4) Click Login
        submit.click()
        time.sleep(5)
        #Verify if user is on dashboard


     def tryandcatch(self):
         try:
             if self.driver.find_element_by_link_text("Dashboard").is_displayed():
                 print("test is successful")
                 Act_Res = self.driver.find_element_by_link_text("Dashboard").text
                 Exp_result = "Dashboard"
                 assert Exp_result == Exp_result
                 print("User logged in Successfully")
                 time.sleep(4)
                 self.driver.find_element_by_id('welcome').click()
                 time.sleep(2)
                 self.driver.find_element_by_link_text('Logout').click()
         except:
                 time.sleep(5)
                 # text = self.driver.find_element_by_id("spanMessage")
                 # print(text)
                 print("test is un-successful")
                 Act_msg = self.driver.find_element_by_id("spanMessage").text
                 assert Exp_result == Act_msg

                 print("test is un-successful")
                 assert Exp_result == Act_msg
                 assert Exp_result == Act_msg
                 assert Exp_result == Act_msg
                 assert Exp_result == Act_msg


'''
# Launch Browser
browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# Step 2) Navigate to OrangeHRM
browser.get("https://opensource-demo.orangehrmlive.com/")
path = "OrangeHRM_TestData .xlsx"
rows = XLUtils.getRowCount(path, 'SignIn')
for r in range(2, rows + 1):
    username_value = XLUtils.readData(path, 'SignIn', r, 1)
    password_value = XLUtils.readData(path, 'SignIn', r, 2)
    Exp_result = XLUtils.readData(path,'SignIn',r,3)
    # Step 3) Enter UserName and Password
    username = browser.find_element_by_name("txtUsername")
    password = browser.find_element_by_name("txtPassword")
    submit = browser.find_element_by_name("Submit")
    username.send_keys(username_value)
    password.send_keys(password_value)
    # Step 4) Click Login
    submit.click()
    try:
        if browser.find_element_by_link_text("Dashboard").is_displayed():
            print("test is successful")
            Act_Res = self.driver.find_element_by_link_text("Dashboard").text
            Exp_result="Dashboard"
            assert Exp_result == Exp_result
            print("User logged in Successfully")
            time.sleep(4)
            self.driver.find_element_by_id('welcome').click()
            time.sleep(2)
            self.driver.find_element_by_link_text('Logout').click()
    except:
        time.sleep(5)
        #text = self.driver.find_element_by_id("spanMessage")
        #print(text)
        print("test is un-successful")
        Act_msg = self.driver.find_element_by_id("spanMessage").text
        assert Exp_result == Act_msg

        print("test is un-successful")
        assert Exp_result == Act_msg
        assert Exp_result == Act_msg
        assert Exp_result == Act_msg
        assert Exp_result == Act_msg


        
'''








