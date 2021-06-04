from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import unittest






class DragandDrop(unittest.TestCase):

    def testdd(self):

        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.get("https://jqueryui.com/resources/demos/droppable/default.html")

        action = ActionChains(self.browser)

        drag = self.browser.find_element_by_id("draggable")
        drop = self.browser.find_element_by_id("droppable")

        action.drag_and_drop(drag,drop).perform()

        self.browser.close()



