import time

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

# Browser details
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# Launch Chrome browser
browser = webdriver.Chrome(ChromeDriverManager().install())

# Step 2) Navigate to OrangeHRM
browser.get("https://opensource-demo.orangehrmlive.com/")

df = pd.read_excel('LoginData.xlsx', sheet_name='Login')
print(df)
data = pd.DataFrame(df, columns=['uname', 'upass'])
# uname = df['uname']
# upass = df['upass']
# print(uname)
# print(upass)
print(data)
print('Excel Sheet to JSON:', data.to_json(orient='records'))

for index, row in df.iterrows():
    print(row["uname"], row["upass"])
    u_value = row["uname"]
    p_value = row["upass"]
    # Step 3) Search & Enter the Email or Phone field & Enter Password
    username = browser.find_element_by_name("txtUsername")
    password = browser.find_element_by_name("txtPassword")
    submit = browser.find_element_by_name("Submit")
    username.send_keys(u_value)
    password.send_keys(p_value)
    # Step 4) Click Login
    submit.click()
    wait = WebDriverWait(browser, 20)
    page_title = browser.title
    print(page_title)
    assert page_title == "OrangeHRM"
    browser.find_element_by_link_text("Dashboard").is_displayed()
    # Logout from application and verify that user has logged out

    browser.find_element_by_partial_link_text("Welcome").click()
    time.sleep(2)
    browser.find_element_by_link_text("Logout").click()
    browser.find_element_by_id("logInPanelHeading").is_displayed()

browser.quit()