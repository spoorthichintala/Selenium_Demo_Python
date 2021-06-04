
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time



#open chrome browser
driver = webdriver.Chrome()
# set implicit time to 30 seconds
#driver.implicitlyWait(30)
# navigate to the url
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element_by_name("txtUsername").send_keys('Admin')
driver.find_element_by_name("txtPassword").send_keys('admin123')
driver.find_element_by_name("Submit").click()
wait = WebDriverWait(driver, 20)
driver.find_element_by_link_text('Dashboard').is_displayed()
# get the Session id of the Parent
parentGUID = driver.current_window_handle
# click the button to open new window
driver.find_element_by_xpath("//a[@class='help-icon-div']").click()
time.sleep(5)
# get the All the session id of the browsers
allGUID = driver.window_handles
# print the title of the page
print("Page title before Switching : " + driver.title)
print("Total Windows : " + str(len(allGUID)))
# iterate the values in the set
for guid in allGUID:
    # one enter into if blobk if the GUID is not equal to parent window's GUID
    if guid != parentGUID:
        # switch to the guid
        driver.switch_to.window(guid)
        # break the loop
        break

# Click on Sign-In link of OrangeHRM help page
driver.find_element_by_link_text("Sign in").click()
# print the title after switching
print("Page title after Switching to : " + driver.title)
time.sleep(5)
# close the browser
driver.close()
# switch back to the parent window
driver.switch_to.window(parentGUID)
time.sleep(5)
# print the title
print("Page title after switching back to Parent: " + str(driver.find_element_by_link_text("Dashboard").is_displayed()))
driver.close()