import time
import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="orangehrm"
)
# browser = webdriver.ie(executable_path=IEDriverManager().install())
browser = webdriver.Chrome(ChromeDriverManager().install())
# browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# Step 2) Navigate to OrangeHRM
browser.get("https://opensource-demo.orangehrmlive.com/")
mycursor = mydb.cursor()
mycursor.execute("select * from login")
myresult = mycursor.fetchall()
print(myresult)
for column in myresult:
    print(column)
    browser.find_element_by_name("txtUsername").send_keys(column[0])
    browser.find_element_by_name("txtPassword").send_keys(column[1])
    browser.find_element_by_name("Submit").click()
    wait = WebDriverWait(browser, 20)
    try:
        if browser.find_element_by_link_text("Dashboard").is_displayed():
            print("test is successful")
            time.sleep(4)
            browser.find_element_by_id('welcome').click()
            time.sleep(2)
            browser.find_element_by_link_text('Logout').click()
    except:
        browser.find_element_by_id('logInPanelHeading').is_displayed()
        print('Login Failed')
mycursor.close()
mydb.close()
browser.quit()