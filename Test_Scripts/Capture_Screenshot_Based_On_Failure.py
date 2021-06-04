import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestDemo(unittest.TestCase):
    """An Example test Case, to show off the set-up of a screen-shot on exception."""
    def setUp(self):
        """Set up the Chrome Browser and the Tear Down."""
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.delete_all_cookies()
        # NOTE: In addCleanup, the first in, is executed last.
        self.addCleanup(self.driver.quit)
        self.addCleanup(self.screen_shot)
        self.driver.implicitly_wait(5)
    def screen_shot(self):
        """Take a Screen-shot of the drive homepage, when it Failed."""
        for method, error in self._outcome.errors:
            if error:
                self.driver.get_screenshot_as_file("Screenshot_Failure/" + self.id() + ".png")
    def test_google_search(self):
        """A test case that fails because of missing element."""
        self.driver.get("http://www.google.com")
        self.driver.find_element_by_name("qq")
    def test_login_to_orangeHRM(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")
        self.driver.find_element(By.NAME, 'txtUsername').send_keys("Admin")
        self.driver.find_element(By.NAME, 'txtPassword').send_keys("admin123")
        self.driver.find_element_by_id('btnLogin').click()

if __name__ == '__main__':
    unittest.main()