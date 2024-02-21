from selenium.webdriver.common.by import By
from behave import then
from selenium.webdriver.support import expected_conditions as EC

CART_ITEM_TITLE = (By.CSS_SELECTOR, 'div[data-test="cartItem-title"]')
CART_SUMMARY = (By.CSS_SELECTOR, 'span[class*="CartSummary"]')
ORDER_SUMMARY = (By.CSS_SELECTOR, 'div[data-test="cart-order-summary"] div[class*="StyledSubheading"]')


@then('Verify "Your cart is empty" message shown')
def verify_cart_is_empty(context):
    context.app.cart_page.verify_empty_cart()


@then('Verify item is displayed in the cart')
def verify_item_in_cart(context):
    context.app.cart_page.verify_item_in_cart()
