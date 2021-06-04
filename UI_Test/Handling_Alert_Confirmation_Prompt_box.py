import time

from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

#Open the browser
browser = webdriver.Chrome(ChromeDriverManager().install())

#Navigate to the URL
browser.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(5)

#Click on JS Alert
browser.find_element_by_xpath("//button[normalize-space()='Click for JS Alert']").click()

#Switch to alert
#browser.switch_to
alert = Alert(browser)
print(alert.text)

#Click on Ok in the Alert
alert.accept()

#Verify the result
actual_text = browser.find_element_by_xpath("//p[@id='result']")
print(actual_text.text)
assert actual_text.text == "You successfully clicked an alert"

#Click on JS Confirm
browser.find_element_by_xpath("//button[normalize-space()='Click for JS Confirm']").click()

#Click on ok in the alert
#alert.accept()
alert.dismiss()
al_text = browser.find_element_by_xpath("//p[@id='result']")
print(al_text.text)

#Verify the Result
#assert al_text.text == "You clicked: Ok"

#Click on JS Prompt
browser.find_element_by_xpath("//button[normalize-space()='Click for JS Prompt']").click()

#Enter text in alert
alert.send_keys("Selenium")
alert.accept()

#Verify the result
s_text = browser.find_element_by_xpath("//p[@id='result']")
print(s_text.text)

act_text = s_text.text

split_text=act_text.split(':')
print(split_text[1])

st= (split_text[1]).strip()
assert st=="Selenium"

browser.close()

