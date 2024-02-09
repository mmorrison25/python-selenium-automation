from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Item is added to cart')
def add_item_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, 'img[alt*="3pc"]').click()
    sleep(3)
    context.driver.find_element(By.CSS_SELECTOR, 'button[aria-label*="Add to cart for 3pc"]').click()
    sleep(3)