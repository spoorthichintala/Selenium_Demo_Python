import time
import unittest
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Main:
#emp_id=4622
    def test_get_id_details(self):
        emp_id = 4622
        r = requests.get("https://chercher.tech/sample/api/product/read?id=" + str(emp_id))
        print(r.json())
        print(r.status_code)
        assert str(200) in str(r.status_code)
        json_string = r.json()
        self.name_value = json_string[0]["name"]
        print(self.name_value)
        return self.name_value
    def test_get_Verify_details(self):
        # Navigate to UI app
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get("https://chercher.tech/sample/api-ui")
        time.sleep(5)
        browser.find_element_by_xpath("//input[@placeholder='Search product...']").send_keys("emp_id")
        act_text = browser.find_element_by_xpath("//td[contains(text(),'Testing')]").text
        time.sleep(3)
        print(act_text)
        self.test_get_id_details()
        print(self.name_value)
        assert self.name_value == act_text
# Instanace of Class Main
Object = Main()
# Calling test_get_Verify_details function
Object.test_get_Verify_details()
# Verify the result using below link
# https://chercher.tech/sample/api-ui