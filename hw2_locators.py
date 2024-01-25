from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from webdriver_manager.core import driver

# Amazon logo
driver.find_element(By.XPATH, "//i [@aria-label='Amazon']")

# Email field
driver.find_element(By.ID, 'ap_email')

# Continue button
driver.find_element(By.ID, 'continue')

# Conditions of Use & Privacy Notice links
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[contains(@href, 'use')]")
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[contains(@href, 'notice')]")

# Need help link
driver.find_element(By.XPATH, "//span [@class='a-expander-prompt']")

# Forgot your pass link
driver.find_element(By.ID, 'auth-fpp-link-bottom')

# Other issues with Sign-In link
driver.find_element(By.ID, 'ap-other-signin-issues-link')

# Create your Amazon account button
driver.find_element(By.ID, 'createAccountSubmit')


