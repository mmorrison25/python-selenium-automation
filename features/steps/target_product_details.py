from selenium.webdriver.common.by import By
from behave import given, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

COLOR_OPTIONS = (By.CSS_SELECTOR, '[class*="ButtonWrapper"] img')
SELECTED_COLOR = (By.CSS_SELECTOR, '[class*="SelectorImage"] [class*="CellVariationHeader"]')


@given('Open product page for {product_id}')
def launch_product_page(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(5)


@then('Verify user can click each of the color options')
def verify_user_select_colors(context):
    expected_colors = ['Beige', 'Black', 'Heather Gray', 'Light Brown']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        selected_color = ' '.join(selected_color.split()[1:])
        actual_colors.append(selected_color)

    assert expected_colors == actual_colors, f'Expected {expected_colors}, got {actual_colors}'