

import xlrd
# Importing necessary modules
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# WebDriver Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())
# Target URL
driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
# Reading Workbook and Sheet
workbook = xlrd.open_workbook("OrangeHRM_TestData.xls")
sheet = workbook.sheet_by_name("SignIn")
# Get number of rows with data in excel sheet
rowcount = sheet.nrows
# Get number of columns with data in each row. Returns highest number
colcount = sheet.ncols
print(rowcount)
print(colcount)
# result_data = []
for curr_row in range(1, rowcount):
# Read the data in the current cell
    user_name_value = sheet.cell_value(curr_row, 0)
    password_value = sheet.cell_value(curr_row, 1)
    print(user_name_value)
    print(password_value)
    # Finding Element
    driver.find_element(By.NAME, 'txtUsername').send_keys(user_name_value)
    driver.find_element(By.NAME, 'txtPassword').send_keys(password_value)
    driver.find_element_by_id('btnLogin').click()
    time.sleep(4)
    driver.find_element_by_id('welcome').click()
    time.sleep(2)
    driver.find_element_by_link_text('Logout').click()
driver.close()

