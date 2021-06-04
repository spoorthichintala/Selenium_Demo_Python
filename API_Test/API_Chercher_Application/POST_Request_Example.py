import time
import requests
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Main:
    def test_student_post_request(self):
        api_url = "https://chercher.tech/sample/api/product/create"
        with open("Post_data.json", "r") as read_file:
            data_pload = json.load(read_file)
            pload = json.dumps(data_pload)
        resp = requests.post(api_url, data = pload)
        print(resp)
        data_returned = resp.text
        print(data_returned)
        assert str(201) in str(resp.status_code)
        # For example, to access the id of the json data:
        print(data_pload["id"])
        self.id_entered = data_pload["id"]
        print(data_pload["name"])
        self.name_entered = data_pload["name"]
        return self.name_entered,self.id_entered

    def test_student_verify_request(self):
        self.test_student_post_request()
        print(self.id_entered)
        print(self.name_entered)
        # Navigate to UI app
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get("https://chercher.tech/sample/api-ui")
        time.sleep(5)
        browser.find_element_by_xpath("//input[@placeholder='Search product...']").send_keys(self.id_entered)
        act_text = browser.find_element_by_xpath("//td[contains(text(),'" + self.name_entered + "')]").text
        time.sleep(3)
        print(act_text)
        assert self.name_entered == act_text

# Instanace of Class Main
Object = Main()
# Calling test_get_Verify_details function
Object.test_student_verify_request()
# Verify the result using below link
# https://chercher.tech/sample/api-ui