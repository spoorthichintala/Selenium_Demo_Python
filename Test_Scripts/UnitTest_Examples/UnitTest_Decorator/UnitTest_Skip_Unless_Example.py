import unittest
import sys
from selenium import webdriver


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        print("Browser Launched")

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    #@unittest.skipIf(sys.platform.startswith("mac"), "requires Windows")
    def test_run_in_windows_only(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        print("Opening OrangeHRM App")

    def tearDown(self):
        self.driver.quit()
        print("Browser Closed")

if __name__ == "__main__":
    unittest.main()
