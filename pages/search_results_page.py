from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):

    ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[id*="addToCartButton"]')
    SEARCH_RESULTS_HEADING = (By.CSS_SELECTOR, 'div[data-test="resultsHeading"]')
    SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[data-test="shippingButton"]')
    VIEW_CART = (By.CSS_SELECTOR, 'a[href="/cart"]')

    def verify_search_results_shown(self, expected_product):
        result_text = self.find_element(*self.SEARCH_RESULTS_HEADING).text
        assert expected_product in result_text, f'Expected word {expected_product} not in {result_text}'

    def add_item_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)
        self.wait_element_clickable_click(*self.SIDE_NAV_ADD_TO_CART_BTN)
        self.wait_element_clickable_click(*self.VIEW_CART)