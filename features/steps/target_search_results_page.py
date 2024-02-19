from selenium.webdriver.common.by import By
from behave import when, then
from selenium.webdriver.support import expected_conditions as EC

SEARCH_RESULTS_HEADING = (By.CSS_SELECTOR, 'div[data-test="resultsHeading"]')
ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[id*="addToCartButton"]')
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[data-test="shippingButton"]')


@when('Add to cart button is clicked')
def add_item_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    context.wait.until(EC.element_to_be_clickable(SIDE_NAV_ADD_TO_CART_BTN)).click()


@then('Search results for {expected_product} are shown')
def verify_search_results_shown(context, expected_product):
    context.app.search_results_page.verify_search_results_shown(expected_product)