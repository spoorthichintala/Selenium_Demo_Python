
import time
import requests
import json

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Main:

    def test_student_Delete_request(self):

        with open("delete_data.json", "r") as read_file:
            data_pload = json.load(read_file)
            pload = json.dumps(data_pload)

        self.id_entered = data_pload["id"]
        api_url = "https://chercher.tech/sample/api/product/delete?id="+ str(self.id_entered)
        resp = requests.put(api_url, pload)
        print(resp)
        data_returned = resp.text
        print(data_returned)
        assert str(200) in str(resp.status_code)


    def test_student_verify_delete_request(self):
        self.test_student_Delete_request()
        print(self.id_entered)
        #print(self.name_entered)
        # Navigate to UI app
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get("https://chercher.tech/sample/api-ui")
        time.sleep(5)
        browser.find_element_by_xpath("//input[@placeholder='Search product...']").send_keys(self.id_entered)
        #act_text = browser.find_element_by_xpath("//td[contains(text(),'" + self.name_entered + "')]").text
        time.sleep(3)
        #print(act_text)
        #assert self.id_entered != act_text
# Instanace of Class Main
Object = Main()

# Calling test_get_Verify_details function
Object.test_student_verify_delete_request()

# Verify the result using below link
# https://chercher.tech/sample/api-ui


