from selenium.webdriver.common.by import By
from pages.base_page import Page


class AcctSideNav(Page):

    SIGN_IN_SIDE_NAV = (By.CSS_SELECTOR, 'a[data-test="accountNav-signIn"]')

    def click_sign_in_side_nav(self):
        self.wait_element_clickable_click(*self.SIGN_IN_SIDE_NAV)