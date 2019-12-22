import logging
from base.basepage import BasePage
from utilities.custom_logger import custom_logger


class NavigationPage(BasePage):

    """
    Page class containing methods used by other page classes for navigation

    Contains methods that interact with web elements
    common to every page

    Arguments:
        None

    Attributes:
        log(obj): Logger instance
    """

    log = custom_logger(logging.INFO)

    # locators
    _login_link = "a.login"
    _store_menu = ".submenu-container a"

    def click_login_link(self):
        self.click_element(self._login_link, "css")

    def click_clothes_menu_link(self, clothes_type):
        self.click_category_type_element(self._store_menu, clothes_type)
