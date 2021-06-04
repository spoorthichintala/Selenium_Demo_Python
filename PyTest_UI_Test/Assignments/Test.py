import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver




driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
# Step 3) Enter the Username & Enter Password
username =driver.find_element_by_name("txtUsername")
password =driver.find_element_by_name("txtPassword")
submit = driver.find_element_by_name("Submit")
username.send_keys("Admin")
password.send_keys("admin123")
# Step 4) Click Login
submit.click()
time.sleep(5)
text1 = driver.find_element_by_id("spanMessage")
captured_text1 = text1.text
print(captured_text1)
assert text1 == "Invalid credentials"
print("Captured Text is equal to expected test")
#Verify if user is on dashboard
#wait = WebDriverWait(self.driver, 20)
dashboard = driver.find_element_by_link_text('Dashboard').is_displayed()
actual_text="Dashboard"
