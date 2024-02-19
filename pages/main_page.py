from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):

    CART_ICON = (By.CSS_SELECTOR, 'div [data-test="@web/CartIcon"]')

    def open_main(self):
        self.open('https://www.target.com/')

    def click_cart(self):
        self.click(*self.CART_ICON)