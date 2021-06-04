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

#Click on cancel
Cancel=browser.find_element_by_id("btnCancel").click()

#Verify the User in webtable
rows = browser.find_elements_by_xpath("//table[@id='resultTable']/tbody/tr")
rowsLength = len(rows)
print("Total number of rows =" + str(rowsLength))

# Complete xpath to get first value "//*[@id='resultTable']/tbody/tr[]/td[2]"
beforXpath = "//*[@id='resultTable']/tbody/tr["
AfterXpath = "]/td[2]"
i = 1
for row in range(rowsLength):
    name = browser.find_element_by_xpath(beforXpath + str(i) + AfterXpath).text
    #print(name)

    if text not in name:
        #browser.find_element_by_xpath("//*[@id='resultTable']/tbody/tr[" + str(i) + "]/td[1]/input").click()
        print(text + " User is not present in row" +  str(i) +"---"+ " Value in row "+str(i)+" is "+name)
        i = i + 1


time.sleep(5)



#Close the browser
browser.quit()



