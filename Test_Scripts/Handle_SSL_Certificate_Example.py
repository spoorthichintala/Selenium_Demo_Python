
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


opts = Options()
# Option 1
'''opts.add_argument('--allow-running-insecure-content')
opts.add_argument('--ignore-certificate-errors')'''

#Option 2
opts.set_capability("acceptInsecureCerts", True)
opts.add_argument('incognito')
# create a new Chrome session
driver = webdriver.Chrome(ChromeDriverManager().install(), options=opts)

# Target URL
driver.get("https://expired.badssl.com/")
#assert self.driver.title() == 'expired.badssl.com'
driver.implicitly_wait(5000)
titleOfWebPage = driver.title
assert('expired.badssl.com',titleOfWebPage,'webpage title is not matching')

# close the browser window
driver.quit()
