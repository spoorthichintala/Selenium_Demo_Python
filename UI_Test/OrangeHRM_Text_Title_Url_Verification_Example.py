import time
import unittest

from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class Verify_dashboard():
    # Step 1) Open Firefox
    browser = webdriver.Chrome(ChromeDriverManager().install())

    # Step 2) Navigate to OrangeHRM
    browser.get("https://opensource-demo.orangehrmlive.com/")
    # Step 3) Search & Enter the Email or Phone field & Enter Password
    username = browser.find_element_by_name("txtUsername")
    password = browser.find_element_by_name("txtPassword")
    submit = browser.find_element_by_name("Submit")
    username.send_keys("Admin")
    password.send_keys("admin123")
    # Step 4) Click Login
    submit.click()
    time.sleep(3)
    page_title = browser.title
    print(page_title)
    assert page_title == "OrangeHRM"
    # Verify the text of Dashboard
    act_text=browser.find_element_by_xpath("//h1[text()='Dashboard']").text
    assert act_text == "Dashboard"
    # Verify the URL
    act_url=browser.current_url
    print(act_url)
    assert act_url == "https://opensource-demo.orangehrmlive.com/index.php/dashboard"

    # Logout from application and verify that user has logged out

    #browser.find_element_by_link_text("Welcome Paul").click()
    browser.find_element_by_partial_link_text("Welcome").click()
    time.sleep(2)
    browser.find_element_by_link_text("Logout").click()
    time.sleep(3)
    page_title = browser.title
    print(page_title)
    assert page_title == "OrangeHRM"
    # Verify the text of Dashboard
    act_login=browser.find_element_by_id("logInPanelHeading").text
    assert act_login == "LOGIN Panel"
    # Verify the URL
    act_loginurl=browser.current_url
    print(act_loginurl)
    assert act_loginurl == "https://opensource-demo.orangehrmlive.com/index.php/auth/login"

    #Close the browser
    browser.close()

if __name__== '__main__':
    unittest.main