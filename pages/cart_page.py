from lib2to3.fixes.fix_input import context
from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):

    EMPTY_CART = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"] h1[class*="StyledHeading"]')
    ORDER_SUMMARY = (By.CSS_SELECTOR, 'div[data-test="cart-order-summary"] div[class*="StyledSubheading"]')

    def verify_empty_cart(self):
        self.wait_element_visible(*self.EMPTY_CART)
        self.verify_text('Your cart is empty', *self.EMPTY_CART)

    def verify_item_in_cart(self):
        self.wait_element_visible(*self.ORDER_SUMMARY)
        self.verify_text('1 item', *self.ORDER_SUMMARY)