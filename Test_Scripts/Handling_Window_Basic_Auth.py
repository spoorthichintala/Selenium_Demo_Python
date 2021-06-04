'''
Created on Mar 20, 2020
@author: adixit
'''
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# Step 1) Open Firefox
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://admin:admin@the-internet.herokuapp.com/basic_auth");
#browser.maximize_window()
ConfMsg = browser.find_element_by_css_selector('p').text
print(ConfMsg)
ExpMessage = "Congratulations! You must have the proper credentials."
assert ConfMsg == ExpMessage
time.sleep(5)
browser.close()
