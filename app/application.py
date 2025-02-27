from pages.base_page import Page
from pages.acct_side_nav import AcctSideNav
from pages.cart_page import CartPage
from pages.circle_page import CirclePage
from pages.header import Header
from pages.help_page import HelpPage
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.sign_in_page import SignIn


class Application:
    def __init__(self, driver):
        self.page = Page(driver)
        self.acct_side_nav = AcctSideNav(driver)
        self.cart_page = CartPage(driver)
        self.circle_page = CirclePage(driver)
        self.header = Header(driver)
        self.help_page = HelpPage(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.sign_in_page = SignIn(driver)