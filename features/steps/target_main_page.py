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


@when('Sign In option is clicked')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a[data-test="@web/AccountLink"]').click()
    sleep(2)


@when('Sign In is clicked from right side nav menu')
def click_sign_in_from_side_nav(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a[data-test="accountNav-signIn"]').click()
    sleep(2)


@when('Search for {product}')
def search_for_product(context, product):
    context.driver.find_element(By.CSS_SELECTOR, 'input[data-test="@web/Search/SearchInput"]').send_keys(product)
    context.driver.find_element(By.CSS_SELECTOR, 'button[data-test="@web/Search/SearchButton"]').click()
    sleep(5)
