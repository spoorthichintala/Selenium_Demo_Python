# Import the 'modules' that are required for execution

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
import sys


@pytest.mark.parametrize(
    "test_browser, test_url",
    [
        pytest.param("firefox", "https://www.google.co.in/", marks=pytest.mark.xfail),
        pytest.param("chrome", "https://opensource-demo.orangehrmlive.com/index.php/auth/login", marks=pytest.mark.basic),
        pytest.param("safari", "https://the-internet.herokuapp.com/javascript_alerts", marks=pytest.mark.skip),
    ]
)
def test_open_url(test_browser, test_url):
    if test_browser == "firefox":
        web_driver = webdriver.Firefox()
        web_driver.get(test_url)
        web_driver.maximize_window()

        title = "Google"
        assert title == web_driver.title

        search_text = "ISTQB"
        search_box = web_driver.find_element_by_xpath("//input[@name='q']")
        search_box.send_keys(search_text)

        time.sleep(5)

        # Option 1 - To Submit the search
        # search_box.submit()

        # Option 2 - To Submit the search
        search_box.send_keys(Keys.ARROW_DOWN)
        search_box.send_keys(Keys.ARROW_UP)
        time.sleep(2)
        search_box.send_keys(Keys.RETURN)

        time.sleep(5)

        # Click on the LambdaTest HomePage Link
        title = "Certifying Software Testers Worldwide - ISTQB® International Software Testing Qualifications Board"
        lt_link = web_driver.find_element_by_xpath(
            "//h3[contains(text(),'Certifying Software Testers Worldwide - ISTQB® Int')]")
        lt_link.click()

        time.sleep(5)
        assert title == web_driver.title
        time.sleep(2)

    if test_browser == "chrome":
        web_driver = webdriver.Chrome()
        web_driver.get(test_url)
        # Step 3) Enter the Username & Enter Password
        username = web_driver.find_element_by_name("txtUsername")
        password = web_driver.find_element_by_name("txtPassword")
        submit = web_driver.find_element_by_name("Submit")
        username.send_keys("Admin")
        password.send_keys("admin123")
        # Step 4) Click Login
        submit.click()
        time.sleep(3)
        # Logout from application
        web_driver.find_element_by_id("welcome").click()
        time.sleep(3)
        web_driver.find_element_by_link_text("Logout").click()
        time.sleep(2)

    web_driver.close()
