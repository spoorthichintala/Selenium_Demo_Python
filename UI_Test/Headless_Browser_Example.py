import time

from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager



opt= Options()
#opt.headless
#opt.set_headless(True)
#opt.__setattr__('headless',True)
opt.add_argument('incognito')

browser = webdriver.Chrome(ChromeDriverManager().install(),options=opt)





browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
username=browser.find_element_by_xpath("//input[@name='txtUsername']")
password=browser.find_element_by_xpath("//input[@name='txtPassword']")
login=browser.find_element_by_xpath("//input[@id='btnLogin']")



username.send_keys("Admin")
password.send_keys("admin123")
login.click()


time.sleep(5)
page_title = browser.title
print(page_title)
assert page_title =="OrangeHRM"


actual_title=browser.find_element_by_link_text("Dashboard").is_displayed()
print(actual_title)
browser.close()