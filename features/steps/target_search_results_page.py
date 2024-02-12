from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_RESULTS_HEADING = (By.CSS_SELECTOR, 'div[data-test="resultsHeading"]')


@then('Search results for {expected_product} are shown')
def verify_search_results_shown(context, expected_product):
    result_text = context.driver.find_element(*SEARCH_RESULTS_HEADING).text
    assert expected_product in result_text, f'Expected word {expected_product} not in {result_text}'
    print('Test case passed')