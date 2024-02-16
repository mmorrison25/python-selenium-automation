from selenium.webdriver.common.by import By
from behave import then
from selenium.webdriver.support import expected_conditions as EC

SIGN_IN_HEADER = (By.CSS_SELECTOR, 'h1 span')


@then('Sign In form opened')
def verify_sign_in_form_opened(context):
    context.wait.until(EC.visibility_of_element_located(SIGN_IN_HEADER), message='Error loading Sign In page')
    sign_in_header = context.driver.find_element(*SIGN_IN_HEADER).text
    assert sign_in_header == 'Sign into your Target account'
    print('Test case passed')