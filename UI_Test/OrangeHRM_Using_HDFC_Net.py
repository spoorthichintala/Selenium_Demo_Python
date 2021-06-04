import time

from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager

#browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
browser = webdriver.Chrome(ChromeDriverManager().install())
#browser = webdriver.Ie(IEDriverManager().install())
#browser= webdriver.Edge(EdgeChromiumDriverManager().install())




browser.get("https://netbanking.hdfcbank.com/netbanking/")
browser.switch_to.frame("login_page")
userid=browser.find_element_by_xpath("//input[@name='fldLoginUserId']")
cont=browser.find_element_by_xpath("//img[@alt='continue']")

userid.send_keys(1000)
browser.switch_to.default_content()
browser.switch_to.frame(1)
terms = browser.find_element_by_link_text("Terms and Conditions")

terms.click()
#cont.click()

time.sleep(5)




#browser.close()