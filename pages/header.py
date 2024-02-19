from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class Header(Page):
    SEARCH_FIELD = (By.CSS_SELECTOR, 'input[data-test="@web/Search/SearchInput"]')
    SEARCH_ICON = (By.CSS_SELECTOR, 'button[data-test="@web/Search/SearchButton"]')
    CART_ICON = (By.CSS_SELECTOR, 'div [data-test="@web/CartIcon"]')

    def search_product(self):
        self.input_text('bedding', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_ICON)
        sleep(5)

    def click_cart(self):
        self.click(*self.CART_ICON)