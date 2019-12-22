import logging
from base.basepage import BasePage
from utilities.custom_logger import custom_logger


class ForgottenPasswordPage(BasePage):

    """
    Page class representing the forgotten password page

    Contains methods that interact with web elements
    located on the forgotten password page

    Arguments:
        None

    Attributes:
        log: Logger instance
    """

    log = custom_logger(logging.INFO)

    # locators
    _email_input = "email"
    _retrieve_password_button = "button.btn.btn-default.button.button-medium"
    _retrieve_password_success_message = "p.alert.alert-success"
    _retrieve_password_error_message = "div.alert.alert-danger"
    _back_to_login_button = "[title='Back to Login']"

    def verify_forgotten_password_page_title(self):
        return self.verify_page_title("Forgot your password - My Store")

    def enter_retrieve_password_email_input(self, username):
        self.sending_keys(username, self._email_input)

    def click_retrieve_password_button(self):
        self.click_element(self._retrieve_password_button, "css")

    def retrieve_password(self, username):
        self.enter_retrieve_password_email_input(username)
        self.click_retrieve_password_button()

    def click_back_to_login_button(self):
        self.click_element(self._back_to_login_button, "css")

    def verify_valid_password_retrieval(self, *args):
        return self.is_text_present(
            self._retrieve_password_success_message, "css",
            "A confirmation email has been sent "
            "to your address: tester123@gmail.com")

    def verify_invalid_password_retrieval(self, *args):
        return self.is_text_present(self._retrieve_password_error_message,
                                    "css", *args, selector="li")
