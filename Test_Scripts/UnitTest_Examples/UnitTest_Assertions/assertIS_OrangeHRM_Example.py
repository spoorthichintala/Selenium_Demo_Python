import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class TestListElements(unittest.TestCase):
    def setUp(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # Target URL
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        time.sleep(5)
    def test_assert_in(self):
        Act_Text = self.driver.title
        print(Act_Text)
        Exp_Text1 = "HRM"
        Exp_Text2 = "ABHI"
        # assertIs() to check that if first & second evaluated to same object
        self.assertIn(Exp_Text1, Act_Text, "Text is not in container")
        self.assertNotIn(Exp_Text2, Act_Text, "Text is not in container")
    def tearDown(self):
        # close the browser window
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()