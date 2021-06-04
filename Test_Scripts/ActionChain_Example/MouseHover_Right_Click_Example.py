import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("MouseHover_Yatra_Example.py")
browser.maximize_window()



source = browser.find_element_by_xpath("//span[@class='context-menu-one btn btn-neutral']")
action = ActionChains(browser)
action.context_click(source).perform()
browser.find_element_by_link_text("//span[normalize-space()='Copy']").click()

time.sleep(5)
alert = Alert(browser)
actual_text = alert.text
print(actual_text)
expected_text = 'clicked: copy'

assert actual_text == expected_text

browser.close()

'''

'''
#Created on Mar 20, 2020
#@author: adixit
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
# Step 1) Open Firefox
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#get method to launch the URL
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
# identifying the source element
source= driver.find_element_by_xpath("//span[text()='right click me']")
# action chain object creation
actionChains = ActionChains(driver)
# right click operation and then perform
actionChains.context_click(source).perform()
driver.find_element_by_xpath("//span[text()='Copy']").click()
sleep(5)
ActTest = driver.switch_to.alert
ActTest1 = ActTest.text
print(ActTest1)
ExpTest="clicked: copy"
assert ActTest1 == ExpTest
ActTest.accept()
#to close the browser
driver.close()

'''