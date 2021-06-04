import random
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

#intialization of browser
browser= webdriver.Chrome(ChromeDriverManager().install())

#Open URL
browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
browser.maximize_window()

#To Verify User is on Login Page
Actual_label=browser.find_element_by_id("logInPanelHeading").text
print(Actual_label)
Expected_label="LOGIN Panel"
assert Actual_label==Expected_label

#Login with Valid Credentials
browser.find_element_by_id("txtUsername").send_keys("Admin")
browser.find_element_by_id("txtPassword").send_keys("admin123")
browser.find_element_by_id("btnLogin").click()
time.sleep(10)

#Verify if User has Logged in
Dashboard=browser.find_element_by_link_text("Dashboard").text
exp = "Dashboard"
if exp in Dashboard:
    print("User is on Dashboard page")
else:
    print("User is not on Dashboard")

#Click on Admin and add the user details

browser.find_element_by_link_text("Admin").click()
browser.find_element_by_id("btnAdd").click()

#get the default value
userrole_dd=Select(browser.find_element_by_id("systemUser_userType"))
userrole_dd.select_by_visible_text("Admin")

#Enter the Value in the Emp name field
emp_name=browser.find_element_by_id("systemUser_employeeName_empName").send_keys("Fiona Grace")
actions =ActionChains(browser)
time.sleep(2)
actions.send_keys(Keys.TAB)
randomnum= random.randint(11,1000)
user_name = browser.find_element_by_id("systemUser_userName").send_keys("Orange"+ str(randomnum))
text =browser.find_element_by_id("systemUser_userName").get_property("value")

#Select the Status
status_dd=Select(browser.find_element_by_id("systemUser_status"))
status_dd.select_by_visible_text("Disabled")

#Enter Password
password =browser.find_element_by_id("systemUser_password").send_keys("admin123")
Confirm_Password=browser.find_element_by_xpath("//input[@id='systemUser_confirmPassword']").send_keys("admin123")
Save=browser.find_element_by_id("btnSave").click()

#Verify the Specific Search
time.sleep(5)
browser.find_element_by_id("searchSystemUser_userName").send_keys(text)

#Verify the default Value in the dropdown User Role and select the User role
Userrole_dd=Select(browser.find_element_by_id("searchSystemUser_userType"))
default_userrole_value=Userrole_dd.first_selected_option
print("Default value of the user type dropdown is : " + default_userrole_value.text)

default_value_userroledd="All"
assert default_userrole_value.text ==default_value_userroledd
Userrole_dd.select_by_visible_text("Admin")

#Verify the default Value in the Employee name and Enter the Name in the textbox
default_emp_name=browser.find_element_by_id("searchSystemUser_employeeName_empName").get_property("value")
print("Default Value in the Employee name field is: "+ default_emp_name)
emp_name=browser.find_element_by_id("searchSystemUser_employeeName_empName").send_keys("Fiona Grace")
actions.send_keys(Keys.TAB)
time.sleep(5)

#Verify the default value in the status dropdown and select the status
Status_dd=Select(browser.find_element_by_id("searchSystemUser_status"))
search_status_default=Status_dd.first_selected_option
print("Default Value in search dropdown is:" + search_status_default.text)
def_text="All"
assert search_status_default.text ==def_text

Status_dd.select_by_visible_text("Disabled")

#Click on Search
browser.find_element_by_id("searchBtn").click()

#Verify the added user in the webtable
browser.get_screenshot_as_png()
web_table=browser.page_source
if text in web_table:
    print(text+" User present in webtable")
else:
    print(text + " User not present in webtable")

#Verify the User in webtable
rows = browser.find_elements_by_xpath("//table[@id='resultTable']/tbody/tr")
rowsLength = len(rows)
print("Total number of rows with specific search = " + str(rowsLength))

#Close the browser

browser.quit()

'''

#Negative scenario
Status_dd=Select(browser.find_element_by_id("searchSystemUser_status"))
search_status_default=Status_dd.first_selected_option
print("Default Value in search dropdown is:" + search_status_default.text)
def_text="All"
assert search_status_default.text ==def_text

Status_dd.select_by_visible_text("Enabled")

#Click on Search
browser.find_element_by_id("searchBtn").click()

    
#Verify the User in webtable
rows = browser.find_elements_by_xpath("//table[@id='resultTable']/tbody/tr")
rowsLength = len(rows)
print("Total number of rows = " + str(rowsLength))
before_xpath="//table[@id='resultTable']/tbody/tr["
after_xpath="]/td"
i=1
for rows in range(rowsLength):
    name=browser.find_element_by_xpath(before_xpath+str(i)+after_xpath).text
    
    i=i+1
    if text in name:
       print(text+" User present in webtable")
else:
   print(name)
browser.quit()
'''
