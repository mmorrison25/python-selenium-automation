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
    context.wait.until(EC.visibility_of_element_located(SEARCH_RESULTS_HEADING), message='Unable to locate search '
                                                                                         'results heading')
    result_text = context.driver.find_element(*SEARCH_RESULTS_HEADING).text
    assert expected_product in result_text, f'Expected word {expected_product} not in {result_text}'
    print('Test case passed')