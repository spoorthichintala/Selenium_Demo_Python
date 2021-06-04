import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


#initialize the browser
browser = webdriver.Chrome(ChromeDriverManager().install())

#Open the URL
browser.get("https://www.testandquiz.com/selenium/testing.html")

#Verify the title of the page
actual_title = browser.title
expected_title ="Sample Test Page"
if actual_title ==expected_title:
    print("Title is matching")
else:
    print("Title is not matching")

#Verify the Heading of the page
heading = browser.find_element_by_xpath("//div[normalize-space()= 'Sample WebPage for Automation Testing']")
heading.text
print(heading.text)
actual_text = "Sample WebPage for Automation Testing"
assert heading.text == actual_text


#Verify text
sample_text= browser.find_element_by_xpath("//b[normalize-space()='This is sample text.']").is_displayed()

#click on link
browser.find_element_by_link_text("This is a link").click()

browser.back()
time.sleep(10)

#enter test in the text field
browser.find_element_by_id("fname").send_keys("Testing")
browser.find_element_by_id("idOfButton").click()

#select radiobutton
radiobutton = browser.find_element_by_id("male")
if radiobutton.is_selected():
    print("radio button is already selected")
else:
    radiobutton.click()
    print("Radio button is selected now")

#Verify and Click on the checkbox
check_box= browser.find_element_by_xpath("//input[@value='Automation']")

if check_box.is_selected():
    print("Check box is enabled")
else:
    check_box.click()


#Dropdown selection
dd=Select(browser.find_element_by_xpath("//select[@id='testingDropdown']"))

default_option = dd.first_selected_option
print("Default option in the dropdown is " + default_option.text)
dd.select_by_index(1)

#Handling Alerts
action = ActionChains(browser)
dc= browser.find_element_by_id("dblClkBtn")
action.double_click(dc).perform()

alert = Alert(browser)
print(alert.text)
alert.accept()



