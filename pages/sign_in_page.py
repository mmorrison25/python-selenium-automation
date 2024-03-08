from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignIn(Page):

    EMAIL_FIELD = (By.CSS_SELECTOR, '[id="username"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '[id="password"]')
    SIGN_IN_HEADER = (By.CSS_SELECTOR, 'h1 span')
    SIGN_IN_BTN = (By.CSS_SELECTOR, '[id="login"]')
    TERMS_CONDITIONS = (By.CSS_SELECTOR, '[aria-label*="terms & conditions"]')
    VALIDATION_MSG = (By.CSS_SELECTOR, '[data-test="authAlertDisplay"]')

    def verify_sign_in_page_opened(self):
        self.wait_element_visible(*self.SIGN_IN_HEADER)
        self.verify_text('Sign into your Target account', *self.SIGN_IN_HEADER)

    def click_terms_and_conditions_link(self):
        self.click(*self.TERMS_CONDITIONS)

    def verify_terms_and_conditions_page_opened(self):
        self.verify_partial_url('https://www.target.com/c/terms-conditions')

    def enter_incorrect_login_credentials(self):
        self.click(*self.EMAIL_FIELD)
        self.input_text('test_1@example.com', *self.EMAIL_FIELD)
        self.click(*self.PASSWORD_FIELD)
        self.input_text('qwerty1234', *self.PASSWORD_FIELD)

    def click_sign_in_button(self):
        self.click(*self.SIGN_IN_BTN)

    def verify_validation_message(self):
        self.wait_element_visible(*self.VALIDATION_MSG)
        self.verify_text("We can't find your account.", *self.VALIDATION_MSG)