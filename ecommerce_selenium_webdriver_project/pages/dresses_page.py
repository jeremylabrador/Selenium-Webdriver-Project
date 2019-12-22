import logging
from base.basepage import BasePage
from utilities.custom_logger import custom_logger
from pages.navigation_page import NavigationPage


class DressesPage(BasePage):

    """
    Page class representing the dresses page

    Contains methods that interact with web elements
    located on the dresses page

    Arguments:
        driver(obj): Webdriver instance

    Attributes:
        log(obj): Logger instance
        driver(obj): Webdriver instance
        nav(obj): NavigationPage instance
    """

    log = custom_logger(logging.INFO)

    # locators
    _store_menu = '.lnk_view'
    _chiffon_dress_link = "li:nth-child(5) h5:nth-child(1) > a.product-name"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    def verify_dresses_page_title(self):
        return self.wait_for_title("Dresses - My Store")

    def navigate_to_dresses_page(self):
        self.nav.click_clothes_menu_link("dresses")
        return self.verify_dresses_page_title()

    def click_chiffon_dress_link(self):
        element = self.wait_for_element_to_be_clickable(
            self._chiffon_dress_link, "css")
        self.click_element(element=element)
