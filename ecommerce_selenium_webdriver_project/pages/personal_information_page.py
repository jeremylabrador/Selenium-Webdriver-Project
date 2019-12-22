import logging
from base.basepage import BasePage
from utilities.custom_logger import custom_logger


class PersonalInformationPage(BasePage):

    """
    Page class representing the personal information page

    Contains methods that interact with web elements
    located on the personal information page

    Arguments:
        None

    Attributes:
        log: Logger instance
    """

    log = custom_logger(logging.INFO)

    # locators
    _old_password_input = "old_passwd"
    _new_password_input = "passwd"
    _confirm_new_password_input = "confirmation"
    _save_button = "submitIdentity"
    _changed_password_successful = "p.alert.alert-success"

    def enter_old_password_input(self, old_password):
        self.sending_keys(old_password, self._old_password_input)

    def enter_new_password_input(self, new_password):
        self.sending_keys(new_password, self._new_password_input)

    def confirm_new_password_input(self, confirmed_password):
        self.sending_keys(confirmed_password, self._confirm_new_password_input)

    def click_save_button(self):
        self.click_element(self._save_button, "name")

    def change_password(self, old_password, new_password, confirmed_password):
        self.enter_old_password_input(old_password)
        self.enter_new_password_input(new_password)
        self.confirm_new_password_input(confirmed_password)
        self.click_save_button()

    def Verify_valid_password_change(self):
        return self.is_text_present(self._changed_password_successful, "css",
                                    "Your personal information has "
                                    "been successfully updated.")
