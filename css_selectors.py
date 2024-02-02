from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# CSS selectors

# Amazon logo
driver.find_element(By.CSS_SELECTOR, 'a.a-link-nav-icon')

# Create account
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

# Name field
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')

# Number/email field
driver.find_element(By.CSS_SELECTOR, '#ap_email')

# Password field
driver.find_element(By.CSS_SELECTOR, '#ap_password')

# Re-enter password field
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

# Continue button
driver.find_element(By.CSS_SELECTOR, 'input.a-button-input')

# Conditions of Use link
driver.find_element(By.CSS_SELECTOR, '#legalTextRow [href*="condition"]')

# Privacy Notice link
driver.find_element(By.CSS_SELECTOR, '#legalTextRow [href*="privacy"]')

# Sign in link
driver.find_element(By.CSS_SELECTOR, '.a-link-emphasis[href*="signin"]')