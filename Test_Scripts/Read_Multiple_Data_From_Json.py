import json
# Importing necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
# WebDriver Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())
# Reading data from JSON file
jsonfile = open('TestData_Multiple.json','r')
jsondata = jsonfile.read()
#Parse
data = json.loads(jsondata)
print(data)
# Here will store data in list(array), which will hold all value from Login_details section
list=data['Login_details']
print(list)
print(len(list))
# Iterating through the json
# list
for i in range(len(list)):
# Target URL
    url = list[i].get('url')
    uname = list[i].get('uname')
    upass = list[i].get('upass')
    print(url)
    print(uname)
    print(upass)
    driver.get(url)
    driver.maximize_window()
    username = driver.find_element(By.NAME, 'txtUsername')
    password = driver.find_element(By.NAME, 'txtPassword')
    LoginButton = driver.find_element_by_id('btnLogin')
    username.send_keys(uname)
    password.send_keys(upass)
    LoginButton.click()
    driver.find_element_by_link_text("Dashboard").is_displayed()
    driver.find_element(By.ID, 'welcome').click()
    driver.implicitly_wait(2)  # seconds
    driver.find_element(By.LINK_TEXT, 'Logout').click()
    driver.implicitly_wait(5)  # seconds
    driver.find_element_by_id('logInPanelHeading').is_displayed()
driver.close()