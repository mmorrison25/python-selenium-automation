from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignIn(Page):

    SIGN_IN_HEADER = (By.CSS_SELECTOR, 'h1 span')

    def verify_sign_in_form_opened(self):
        self.wait_element_visible(*self.SIGN_IN_HEADER)
        self.verify_text('Sign into your Target account', *self.SIGN_IN_HEADER)
