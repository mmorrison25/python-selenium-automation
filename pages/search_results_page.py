from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS_HEADING = (By.CSS_SELECTOR, 'div[data-test="resultsHeading"]')

    def verify_search_results_shown(self, expected_product):
        result_text = self.find_element(*self.SEARCH_RESULTS_HEADING).text
        assert expected_product in result_text, f'Expected word {expected_product} not in {result_text}'