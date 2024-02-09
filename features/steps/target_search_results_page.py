from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Search results for {expected_product} are shown')
def verify_search_results_shown(context, expected_product):
    result_text = context.driver.find_element(By.CSS_SELECTOR, 'div[data-test="resultsHeading"]').text
    assert expected_product in result_text, f'Expected word {expected_product} not in {result_text}'
    print('Test case passed')