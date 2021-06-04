import time

from selenium import webdriver




#browser = webdriver.Chrome()
browser = webdriver.Firefox()



browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
browser.find_element_by_name("txtUsername").send_keys("Admin")
browser.find_element_by_name("txtPassword").send_keys("admin123")
browser.find_element_by_id("btnLogin").click()

time.sleep(5)
page_title = browser.title
print(page_title)
assert page_title =="OrangeHRM"


actual_title=browser.find_element_by_link_text("Dashboard").is_displayed()
print(actual_title)
browser.close()