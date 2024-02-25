from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BENEFIT_BOX = (By.CSS_SELECTOR, 'li[class*="styles__BenefitCard"]')


@given('Target Circle page is launched')
def open_circle_page(context):
    context.app.circle_page.open_circle_page()


@then('Verify clicking through Circle tabs works')
def verify_click_through_circle_tabs(context):
    context.app.circle_page.verify_click_through_circle_tabs()


@then('Verify {expected_amount} benefit boxes are displayed')
def verify_target_benefits_are_displayed(context, expected_amount):
    expected_amount = int(expected_amount)
    benefit_boxes = context.driver.find_elements(*BENEFIT_BOX)
    assert len(benefit_boxes) == expected_amount, f'Expected {expected_amount} boxes but got {len(benefit_boxes)}'