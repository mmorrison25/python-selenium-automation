from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class Header(Page):
    CART_ICON = (By.CSS_SELECTOR, 'div [data-test="@web/CartIcon"]')
    SEARCH_FIELD = (By.CSS_SELECTOR, 'input[data-test="@web/Search/SearchInput"]')
    SEARCH_ICON = (By.CSS_SELECTOR, 'button[data-test="@web/Search/SearchButton"]')
    SIGN_IN_ICON = (By.CSS_SELECTOR, 'a[data-test="@web/AccountLink"]')

    def search_product(self):
        self.input_text('bedding', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_ICON)
        sleep(5)

    def click_cart(self):
        self.click(*self.CART_ICON)

    def click_sign_in_icon(self):
        self.click(*self.SIGN_IN_ICON)