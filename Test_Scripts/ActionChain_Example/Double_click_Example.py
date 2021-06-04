import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import Select
#launch browser
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.testandquiz.com/selenium/testing.html")
heading = browser.find_element_by_xpath("//div[@class='col-md-offset-2 col-md-8']")
actual_text =heading.text
expected_text ="Sample WebPage for Automation Testing"
assert actual_text == expected_text
#click link
browser.find_element_by_link_text("This is a link").click()
actual_url =browser.current_url
expected_url ="https://www.javatpoint.com/"
assert actual_url ==expected_url
browser.implicitly_wait(10)
browser.back()
#Text Box
# wait =WebDriverWait(browser,10)
# wait.until(EC.presence_of_element_located(By.ID('fname')))
browser.implicitly_wait(5)
browser.find_element_by_id("fname").send_keys("Textmessage")
#BUtton
browser.find_element_by_id("idOfButton").click()
#radiobutton
ele =browser.find_element_by_id("female")
ele.click()
if ele.is_selected():
    print("radio button selected")
else:
    print("radio button not selected")
#checkbox
browser.find_element_by_xpath("//input[@value='Performance']").click()
#Defautl drop down value
ele =Select(browser.find_element_by_xpath("//select[@id='testingDropdown']"))
default_option=ele.first_selected_option
first_selected = default_option.text
assert first_selected == "Automation Testing"
#DropDown
dropdown = Select(browser.find_element_by_xpath("//select[@id='testingDropdown']"))
dropdown.select_by_visible_text("Manual Testing")
#Double_click
action = ActionChains(browser)
action.double_click(browser.find_element_by_id("dblClkBtn")).perform()
alert = Alert(browser)
alert_text =alert.text
assert alert_text =="hi, JavaTpoint Testing"
time.sleep(5)
alert.accept()
#confirmation box
browser.find_element_by_xpath("//button[normalize-space()='Generate Confirm Box']").click()
alert =Alert(browser)
time.sleep(5)
alert.accept()
demo_text =browser.find_element_by_id("demo").text
assert demo_text =="You pressed OK!"