from lib2to3.fixes.fix_input import context
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC


class CartPage(Page):

    EMPTY_CART = (By.CSS_SELECTOR, 'h1')

    def verify_empty_cart(self):
        context.wait.until(EC.presence_of_element_located(*self.EMPTY_CART))
        cart_message = self.find_element(*self.EMPTY_CART).text
        assert cart_message == 'Your cart is empty', f'Expected "Your cart is empty", but got "{cart_message}"'