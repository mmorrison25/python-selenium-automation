from selenium.webdriver.common.by import By
from behave import then
from selenium.webdriver.support import expected_conditions as EC

VIEW_CART = (By.CSS_SELECTOR, 'a[href="/cart"]')
CART_ITEM_TITLE = (By.CSS_SELECTOR, 'div[data-test="cartItem-title"]')
CART_SUMMARY = (By.CSS_SELECTOR, 'span[class*="CartSummary"]')
ORDER_SUMMARY = (By.CSS_SELECTOR, 'div[data-test="cart-order-summary"] div[class*="StyledSubheading"]')


@then('Verify "Your cart is empty" message shown')
def verify_cart_is_empty(context):
    context.app.cart_page.verify_empty_cart()


@then('Verify item is displayed in the cart')
def verify_cart_is_displayed(context):
    context.wait.until(EC.element_to_be_clickable(VIEW_CART)).click()
    context.wait.until(EC.presence_of_element_located(ORDER_SUMMARY))
    order_summary = context.driver.find_element(*ORDER_SUMMARY).text
    assert order_summary == '1 item', f"Expected 1 item but got {order_summary}"
    print('Test passed: Item is displayed in the cart')
