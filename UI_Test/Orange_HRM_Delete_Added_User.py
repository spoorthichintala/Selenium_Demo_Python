import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


browser = webdriver.Chrome(ChromeDriverManager().install())
# browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# Step 2) Navigate to OrangeHRM
browser.get("https://opensource-demo.orangehrmlive.com/")

browser.find_element_by_name("txtUsername").send_keys('Admin')
browser.find_element_by_name("txtPassword").send_keys('admin123')
browser.find_element_by_name("Submit").click()
wait = WebDriverWait(browser, 20)
browser.find_element_by_link_text('Dashboard').is_displayed()

#Click on Admin
browser.find_element_by_link_text('Admin').click()
# Click on Add Button
browser.find_element_by_name('btnAdd').click()

#Select Admin from Dropdown Value
dropdown= Select(browser.find_element_by_id('systemUser_userType'))
dropdown.select_by_visible_text('Admin')

browser.find_element_by_id("systemUser_employeeName_empName").send_keys("Fiona Grace")
randomInt = random.randint(0,1000)
browser.find_element_by_id("systemUser_userName").send_keys("abhi" + str(randomInt))

#ExpUserName = browser.find_element_by_id("systemUser_userName").text
browser.find_element_by_id("systemUser_password").send_keys("admin123")
browser.find_element_by_id("systemUser_confirmPassword").send_keys("admin123")
time.sleep(5)
browser.find_element_by_id("btnSave").click()
time.sleep(5)
ExpUserName = "abhi" + str(randomInt)
browser.refresh()
cellvalue = browser.find_element_by_xpath("//a[text()='" + ExpUserName + "']")
#//a[text()='"+ ExpUserName +"']

textvalue = cellvalue.text
print(textvalue)
assert ExpUserName == textvalue
time.sleep(10)

#Delete Added user from WebTable

#browser.find_element_by_xpath("//a[text()='"+ExpUserName+"']/parent::td/preceding-sibling::td/input").click()
browser.find_element_by_xpath("//td/a[text()='"+ExpUserName+"']//parent::td/../td/input").click()
time.sleep(5)
browser.find_element_by_id("btnDelete").click()
browser.find_element_by_id("dialogDeleteBtn").click()
time.sleep(5)
browser.close()