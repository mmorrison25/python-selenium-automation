from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[id*="addToCartButton"]')
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[data-test="shippingButton"]')


@when('Item is added to cart')
def add_item_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(3)
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()
    sleep(3)