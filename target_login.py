from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from webdriver_manager.core import driver

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Test case: User can navigate to Sign In page

# Navigate to Target home page
driver.get('https://www.target.com')

# Click the Sign-In link from top nav
driver.find_element(By.XPATH, "//a[@aria-label='Account, sign in']//span").click()
sleep(2)

# Click the Sign-In link from top nav
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
sleep(2)

# Verify user is on the Sign-In page
sign_in_header = driver.find_element(By.XPATH, "//h1//span").text
assert sign_in_header == 'Sign into your Target account'

# Verify the Sign-In button is present
driver.find_element(By.ID, 'login')

print('Test case passed')
driver.quit()
