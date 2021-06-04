'''Web scraping is the process of collecting and parsing data from the web.
The Python community has come up with some pretty powerful web scrapping tools.
Among them, Pandas read_html() is a quick and convenient way for scraping data from HTML table'''

import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

# Step 2) Navigate to OrangeHRM
browser.get("https://opensource-demo.orangehrmlive.com/")
# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element_by_name("txtUsername")
password = browser.find_element_by_name("txtPassword")
submit = browser.find_element_by_name("Submit")
username.send_keys("Admin")
password.send_keys("admin123")
# Step 4) Click Login
submit.click()
wait = WebDriverWait(browser, 20)
page_title = browser.title
print(page_title)
assert page_title == "OrangeHRM"

browser.find_element_by_link_text("Dashboard").is_displayed()

browser.find_element_by_link_text("Admin").click()

#Grab the web page source
html=browser.page_source

#Pandas read_html() function is a quick and convenient way for scraping data from HTML tables

#Filtering tables with attrs The argument attrs takes a dictionary of any valid HTML tag attributes for filtering tables.
# For example---attrs = { 'id': 'resultTable'}

table_attribute=pd.read_html(html, attrs = { 'id': 'resultTable'})
print(table_attribute)

table_null_value=pd.read_html(html, attrs = { 'id': 'resultTable'},keep_default_na=False)

print(table_null_value)

#Matching a table with match (match='Admin')
#The argument match takes a string or a regular expression.
table_match=pd.read_html(html, attrs = { 'id': 'resultTable'},match='dixit')
print(table_match[0])
uname = table_match[0].loc[:,'Username']
print(uname)

browser.quit()