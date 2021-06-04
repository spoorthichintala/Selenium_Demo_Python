import time

from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager


browser = webdriver.Chrome(ChromeDriverManager().install())



browser.get("https://netbanking.hdfcbank.com/netbanking/")
browser.switch_to.frame("login_page")
#userid=browser.find_element_by_xpath("//input[@name='fldLoginUserId']")

browser.find_element_by_xpath("//img[@alt='continue']").click()
alert_ele = browser.switch_to.alert
alert_text = alert_ele.text

assert alert_text =="Customer ID  cannot be left blank."

time.sleep(2)
browser.close()
'''
userid.send_keys(1000)
browser.switch_to.default_content()
browser.switch_to.frame(1)
terms = browser.find_element_by_link_text("Terms and Conditions")

terms.click()
#cont.click()

time.sleep(5)
'''

