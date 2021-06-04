import time
import pytest
#rom pytest_html_reporter import attach
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.mark.parametrize("uname, upass", [("Admin", "admin123"), ("Admin", "admin123")])
def test_list_valid_user(uname, upass):

    url = "https://opensource-demo.orangehrmlive.com/index.php/auth/login"
    browser = webdriver.Chrome(ChromeDriverManager().install())

    # Step 2) Navigate to OrangeHRM
    browser.get(url)


    # Step 3) Search & Enter the Email or Phone field & Enter Password
    username = browser.find_element_by_name("txtUsername")
    password = browser.find_element_by_name("txtPassword")
    submit = browser.find_element_by_name("Submit")
   #attach(data=browser.get_screenshot_as_png())
    username.send_keys(uname)
    password.send_keys(upass)
    # Step 4) Click Login
    submit.click()
    browser.close()
    '''#Logout from application
    browser.find_element_by_id("welcome").click()
    time.sleep(3)
    browser.find_element_by_("Logout").click()'''

    #browser.find_element_by_link_text("Logout").click()

