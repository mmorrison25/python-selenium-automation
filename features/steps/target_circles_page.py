from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BENEFIT_BOX = (By.CSS_SELECTOR, 'li[class*="styles__BenefitCard"]')


@given('Target circle page is launched')
def open_target_circles_page(context):
    context.driver.get("https://www.target.com/circle")


@then('Verify {expected_amount} benefit boxes are displayed')
def verify_target_benefits_are_displayed(context, expected_amount):
    expected_amount = int(expected_amount)
    benefit_boxes = context.driver.find_elements(*BENEFIT_BOX)
    assert len(benefit_boxes) == expected_amount, f'Expected {expected_amount} boxes but got {len(benefit_boxes)}'