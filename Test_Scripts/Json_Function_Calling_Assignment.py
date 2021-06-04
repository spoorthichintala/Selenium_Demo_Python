import json
# Importing necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from Test_Scripts import Config

# WebDriver Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())
# Reading data from JSON file
file = Config.readJsonData('TestData_Multiple.json','r')

#Parse
data =Config.loadJsonData(file)

# Here will store data in list(array), which will hold all value from Login_details section
getlist=Config.StoreDatainArray(data,'Login_details')

# Iterating through the json

#itteration = Config.IteratingJsonList(list1)
for i in range(len(getlist)):
# Target URL
    url = getlist[i].get('url')
    uname = getlist[i].get('uname')
    upass = getlist[i].get('upass')
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