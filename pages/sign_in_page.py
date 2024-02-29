from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignIn(Page):

    SIGN_IN_HEADER = (By.CSS_SELECTOR, 'h1 span')
    TERMS_CONDITIONS = (By.CSS_SELECTOR, '[aria-label*="terms & conditions"]')

    def verify_sign_in_page_opened(self):
        self.wait_element_visible(*self.SIGN_IN_HEADER)
        self.verify_text('Sign into your Target account', *self.SIGN_IN_HEADER)

    def click_terms_and_conditions_link(self):
        self.click(*self.TERMS_CONDITIONS)

    def verify_terms_and_conditions_page_opened(self):
        self.verify_partial_url('https://www.target.com/c/terms-conditions')