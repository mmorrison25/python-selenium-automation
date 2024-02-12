from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

EMPTY_CART = (By.CSS_SELECTOR, 'h1')
VIEW_CART = (By.CSS_SELECTOR, 'a[href="/cart"]')
CART_ITEM_TITLE = (By.CSS_SELECTOR, 'div[data-test="cartItem-title"]')
CART_SUMMARY = (By.CSS_SELECTOR, 'span[class*="CartSummary"]')
ORDER_SUMMARY = (By.CSS_SELECTOR, 'div[data-test="cart-order-summary"] div[class*="StyledSubheading"]')


@then('Your cart is empty message shown')
def verify_cart_is_empty(context):
    cart_message = context.driver.find_element(*EMPTY_CART).text
    assert cart_message == 'Your cart is empty'
    print('Test passed: Cart is empty')


@then('Item is displayed in the cart')
def verify_cart_is_displayed(context):
    context.driver.find_element(*VIEW_CART).click()
    order_summary = context.driver.find_element(*ORDER_SUMMARY).text
    assert order_summary == '1 item'
    print('Test passed: Item is displayed in the cart')
