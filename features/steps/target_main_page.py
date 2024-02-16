from selenium.webdriver.common.by import By
from behave import given, when
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


CART_ICON = (By.CSS_SELECTOR, 'div [data-test="@web/CartIcon"]')
SIGN_IN_BUTTON = (By.CSS_SELECTOR, 'a[data-test="@web/AccountLink"]')
SIGN_IN_SIDE_NAV = (By.CSS_SELECTOR, 'a[data-test="accountNav-signIn"]')
SEARCH_FIELD = (By.CSS_SELECTOR, 'input[data-test="@web/Search/SearchInput"]')
SEARCH_ICON = (By.CSS_SELECTOR, 'button[data-test="@web/Search/SearchButton"]')


@given('Target site is launched')
def open_target_site(context):
    context.driver.get("https://www.target.com/")


@when('Cart icon is clicked')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()


@when('Sign In option is clicked')
def click_sign_in(context):
    context.driver.find_element(*SIGN_IN_BUTTON).click()


@when('Sign In is clicked from right side nav menu')
def click_sign_in_from_side_nav(context):
    context.wait.until(EC.element_to_be_clickable(SIGN_IN_SIDE_NAV)).click()


@when('Search for {product}')
def search_for_product(context, product):
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    context.driver.find_element(*SEARCH_ICON).click()
    sleep(5)