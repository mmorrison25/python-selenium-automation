from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import Page


class HelpPage(Page):

    HEADER_DELIVERY_PICKUP = (By.XPATH, "//h1[text()=' Drive Up & Order Pickup']")
    HEADER_RETURNS = (By.XPATH, "//h1[text()=' Returns']")
    TOPIC_SELECTION = (By.CSS_SELECTOR, 'select[id*="viewHelpTopic"]')

    def open_help_returns(self):
        self.open('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')

    def select_help_topic(self, topic_name):
        topic_dd = self.find_element(*self.TOPIC_SELECTION)
        select = Select(topic_dd)
        select.select_by_value(topic_name)

    def verify_returns_displayed(self):
        self.wait_element_visible(*self.HEADER_RETURNS)

    def verify_delivery_pickup_displayed(self):
        self.wait_element_visible(*self.HEADER_DELIVERY_PICKUP)