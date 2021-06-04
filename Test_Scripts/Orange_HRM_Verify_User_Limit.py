import datetime
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
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
randomInt = random.randint(11,100)
#print(time.time())
#randomInt = time.time()
username = browser.find_element_by_id("systemUser_userName")
username.send_keys("abhidixitabhidixitabhidixitabhidixitabh" + str(randomInt))

#Verify the MaxLength of UserName Field

EnteredValue = username.get_attribute("value")
EnteredValueSize=len(str(EnteredValue))
print(EnteredValueSize)

if EnteredValueSize == 40:
    print('Maxlength character functionality is 40 and its working fine.')
else:
    print('It allow more than 40')

#ExpUserName = username.text
browser.find_element_by_id("systemUser_password").send_keys("admin123")
browser.find_element_by_id("systemUser_confirmPassword").send_keys("admin123")
time.sleep(5)
browser.find_element_by_id("btnSave").click()
#ExpUserName = "abhi" + str(randomInt)
browser.refresh()
cellvalue = browser.find_element_by_xpath("//a[text()='" + EnteredValue + "']")

textvalue = cellvalue.text
print(textvalue)
assert EnteredValue == textvalue
#Delete Added user from WebTable

browser.find_element_by_xpath("//a[text()='"+EnteredValue+"']//parent::td/../td[text()='Admin']").is_displayed()
browser.find_element_by_xpath("//a[text()='"+EnteredValue+"']//parent::td/../td[text()='Admin']/../td/input").click()
time.sleep(5)
browser.find_element_by_id("btnDelete").click()
browser.find_element_by_id("dialogDeleteBtn").click()
time.sleep(5)
browser.close()