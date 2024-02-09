from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Sign In form opened')
def verify_sign_in_form_opened(context):
    sign_in_header = context.driver.find_element(By.CSS_SELECTOR, 'h1 span').text
    assert sign_in_header == 'Sign into your Target account'
    print('Test case passed')