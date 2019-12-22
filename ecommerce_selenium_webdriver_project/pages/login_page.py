import logging
from base.basepage import BasePage
from utilities.custom_logger import custom_logger
from pages.navigation_page import NavigationPage


class LoginPage(BasePage):

    """
    Page class representing the login page

    Contains methods that interact with web elements
    located on the login page

    Arguments:
        driver(obj): Webdriver instance

    Attributes:
        log(obj): Logger instance
        driver(obj): Webdriver instance
        nav(obj): NavigationPage instance
    """

    log = custom_logger(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.nav = NavigationPage(driver)

    # locators
    _email_input = "email"
    _password_input = "passwd"
    _login_button = "SubmitLogin"
    _login_error_message = "div.alert.alert-danger ol"
    _logged_in = "a.account"
    _forgotten_password_link = "p.lost_password.form-group > a"
    _nav_bar = "nav div a"

    def verify_login_page_title(self):
        return self.verify_page_title("Login - My Store")

    def enter_login_email_input(self, username):
        self.sending_keys(username, self._email_input)

    def enter_login_password_input(self, password):
        self.sending_keys(password, self._password_input)

    def click_login_button(self):
        self.click_element(self._login_button)

    def login(self, username, password):
        self.enter_login_email_input(username)
        self.enter_login_password_input(password)
        self.click_login_button()

    def verify_valid_login(self):
        return self.is_element_present(self._logged_in, "css")

    def verify_invalid_password_error_message(self):
        return self.is_text_present(self._login_error_message,
                                    "css", "Authentication failed.")

    def verify_invalid_login_error_message(self, *args):
        return self.is_text_present(self._login_error_message,
                                    "css", *args, selector="li")

    def remain_logged_out(self):
        self.click_list_element_containing_text(self._nav_bar,
                                                "css", "Sign out")

    def navigate_to_login_page(self):
        self.remain_logged_out()
        self.nav.click_login_link()
        return self.verify_login_page_title()

    def click_forgotten_password_link(self):
        self.click_element(self._forgotten_password_link, "css")

    def navigate_to_forgotten_password_page(self):
        self.remain_logged_out()
        self.nav.click_login_link()
        self.click_forgotten_password_link()
