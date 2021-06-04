import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class SearchText(unittest.TestCase):
    def setUp(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # Target URL
        self.driver.get("https://google.co.in")
    def test_search_by_text(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")
        # enter search keyword and submit
        self.search_field.send_keys("Selenium WebDriver Interview questions")
        self.search_field.submit()
        # get the list of elements which are displayed after the search
        # currently on result page usingfind_elements_by_class_namemethod
        lists = self.driver.find_elements_by_class_name("g")
        no = len(lists)
        print(no)
        self.assertEqual(15, no)
    def tearDown(self):
        # close the browser window
        self.driver.quit()