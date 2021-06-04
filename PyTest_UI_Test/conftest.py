import pytest
import webdriver_manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture()
def driver_init(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome("C:\\Users\\admin\\PycharmProjects\\Selenium_Training\\Browser_Driver\\chromedriver.exe")

    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.close()

@pytest.fixture
def app_url():
	url = "https://opensource-demo.orangehrmlive.com/index.php/auth/login"
	return url
'''
@pytest.fixture(params=["chrome", "firefox"])
def driver_init(request):
	if request.param == "chrome":
		web_driver = webdriver.Chrome()
	if request.param == "firefox":
		web_driver = webdriver.Firefox()
	request.cls.driver = web_driver



	yield
	web_driver.close()

@pytest.fixture
def app_url():
	url = "https://opensource-demo.orangehrmlive.com/index.php/auth/login"
	return url

'''