from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Target site is launched')
def open_target_site(context):
    context.driver.get("https://www.target.com/")
    sleep(2)


@when('Cart icon is clicked')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, 'div [data-test="@web/CartIcon"]').click()
    sleep(2)


@then('Your cart is empty message shown')
def verify_cart_is_empty(context):
    cart_message = context.driver.find_element(By.CSS_SELECTOR, 'h1').text
    assert cart_message == 'Your cart is empty'
    print('Test case passed')


@when('Sign In option is clicked')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a[data-test="@web/AccountLink"]').click()
    sleep(2)


@when('Sign In is clicked from right side nav menu')
def click_sign_in_from_side_nav(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a[data-test="accountNav-signIn"]').click()
    sleep(2)


@then('Sign In form opened')
def verify_sign_in_form_opened(context):
    sign_in_header = context.driver.find_element(By.CSS_SELECTOR, 'h1 span').text
    assert sign_in_header == 'Sign into your Target account'
    print('Test case passed')