from selenium.webdriver.common.by import By
from pages.base_page import Page


class CirclePage(Page):

    TABS = (By.CSS_SELECTOR, '[class*="PageSelectionText"] a')
    BONUS_TAB = (By.CSS_SELECTOR, '[data-test="bonus-tab"]')

    def open_circle_page(self):
        self.open("https://www.target.com/circle")

    def verify_click_through_circle_tabs(self):
        self.wait_element_clickable(*self.BONUS_TAB)
        tabs = self.driver.find_elements(*self.TABS)

        current_url = ''

        for i in range(len(tabs)):
            tabs = self.driver.find_elements(*self.TABS)
            tabs[i].click()

            self.wait_url_changes(current_url)
            current_url = self.driver.current_url