import logging
from base.basepage import BasePage
from utilities.custom_logger import custom_logger


class AccountPage(BasePage):

    """
    Page class representing the account page

    Contains methods that interact with web elements
    located on the account page

    Arguments:
        None

    Attributes:
        log(obj): Logger instance
    """

    log = custom_logger(logging.INFO)

    # locators
    _information_link = "ul.myaccount-link-list li:nth-child(4) > a"

    def click_information_link(self):
        self.click_element(self._information_link, "css")
