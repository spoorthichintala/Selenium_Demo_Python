import random
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager



#launch the browser
browser = webdriver.Chrome(ChromeDriverManager().install())

#Enter the URL
browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
browser.maximize_window()

#Login with valid credentials
browser.find_element_by_id("txtUsername").send_keys("Admin")
browser.find_element_by_id("txtPassword").send_keys("admin123")
browser.find_element_by_id("btnLogin").click()
time.sleep(10)

#Verify if user is on the dashboard
dashboard = browser.find_element_by_link_text("Dashboard")
if dashboard.is_displayed():
    print("user is on dashboard")
else:
    print("user is not on dashboard")

time.sleep(2)
#Click on PIM
browser.find_element_by_link_text("PIM").click()

#Mouse Hover on to configurations
action = ActionChains(browser)
action.move_to_element(browser.find_element_by_link_text("Configuration")).perform()
action.move_to_element(browser.find_element_by_link_text("Custom Fields")).perform()
browser.find_element_by_link_text("Custom Fields").click()
time.sleep(2)
#Add the User
browser.find_element_by_id("buttonAdd").click()

#Add custom Fields
fields_name = browser.find_element_by_id("customField_name")
random_num = random.randint(11,1000)
user_name = fields_name.send_keys("Orange"+ str(random_num))
time.sleep(5)


#Enter the value in the Screen and type dropdown
screen_dd = Select(browser.find_element_by_id("customField_screen"))
default_option = screen_dd.first_selected_option
print(default_option.text)
screen_dd.select_by_value("personal")
type_dd = Select(browser.find_element_by_id("customField_type"))
type_dd.select_by_value("0")
entered_user=fields_name.text
browser.find_element_by_id("btnSave").click()
source = browser.page_source
if entered_user in source:
    print("user entered is present")
else:
    print(entered_user + "user not added in the list")


ExpUserName = "Orange" + str(random_num)
browser.refresh()
cellvalue = browser.find_element_by_xpath("//a[text()='"+ExpUserName+"']")

textvalue = cellvalue.text
print(textvalue)
assert ExpUserName == textvalue
#Delete all users based on matching patern from WebTable

rows = browser.find_elements_by_xpath("//table[@id='customFieldList']/tbody/tr")
rowsLength=len(rows)
print(rowsLength)

# Complete xpath to get first value "//*[@id='resultTable']/tbody/tr[]/td[2]"
beforXpath = "//*[@id='customFieldList']/tbody/tr["
AfterXpath = "]/td[2]"
i=1
for row in range(rowsLength):

    name = browser.find_element_by_xpath(beforXpath + str(i) + AfterXpath).text
    print(name)

    if "Orange" in name:
        browser.find_element_by_xpath("//*[@id='customFieldList']/tbody/tr[" + str(i) + "]/td[1]/input").click()
    i = i + 1
time.sleep(5)

#Delete user
browser.find_element_by_id("buttonRemove").click()
browser.find_element_by_id("dialogDeleteBtn").click()

browser.quit()








