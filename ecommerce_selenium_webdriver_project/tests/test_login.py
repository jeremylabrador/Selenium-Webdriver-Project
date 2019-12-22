import pytest
from pages.account_page import AccountPage
from utilities.assert_status import AssertStatus
from pages.forgotten_password_page import ForgottenPasswordPage
from pages.login_page import LoginPage
from pages.personal_information_page import PersonalInformationPage
from utilities.read_csv_data import get_csv_data


@pytest.mark.usefixtures("one_time_setup", "setup")
class TestLogin():

    @pytest.fixture(autouse=True)
    def object_setup(self):
        self.lp = LoginPage(self.driver)
        self.pip = PersonalInformationPage(self.driver)
        self.ap = AccountPage(self.driver)
        self.fpp = ForgottenPasswordPage(self.driver)
        self.ast = AssertStatus()

    @pytest.mark.parametrize(
        "email, password, email_error_message, password_error_message",
        get_csv_data("login_test_data.csv"))
    def test_invalid_login(
            self, email, password, email_error_message,
            password_error_message):
        result_1 = self.lp.navigate_to_login_page()
        self.ast.collect_result(result_1, "Login Page Title Verification")

        self.lp.login(email, password)
        result_2 = self.lp.verify_invalid_login_error_message(
            email_error_message, password_error_message)
        self.ast.determine_result(
            result_2, "Failed Login Verification", "test_invalid_login")

    def test_valid_login(self):
        result_1 = self.lp.navigate_to_login_page()
        self.ast.collect_result(result_1, "Login Page Title Verification")

        self.lp.login("tester123@gmail.com", "123456")
        result_2 = self.lp.verify_valid_login()
        self.ast.determine_result(
            result_2, "Login Verification", "test_valid_login")

    @pytest.mark.parametrize(
        "email, error_message",
        get_csv_data("retrieve_password_email_test_data.csv"))
    def test_invalid_password_retrieval(self, email, error_message):
        self.lp.navigate_to_forgotten_password_page()
        result_1 = self.fpp.verify_forgotten_password_page_title()
        self.ast.collect_result(
            result_1, "Forgotten Password Page Title Verification")

        self.fpp.retrieve_password(email)
        result_2 = self.fpp.verify_invalid_password_retrieval(error_message)
        self.ast.determine_result(
            result_2, "Failed Password Retrieval Verification",
            "test_invalid_password_retrieval")

    def test_valid_password_retrieval(self):
        self.lp.navigate_to_forgotten_password_page()
        result_1 = self.fpp.verify_forgotten_password_page_title()
        self.ast.collect_result(
            result_1, "Forgotten Password Page Title Verification")

        self.fpp.retrieve_password("tester123@gmail.com")
        result_2 = self.fpp.verify_valid_password_retrieval()
        self.ast.determine_result(
            result_2, "Password Retrieval Verification",
            "test_valid_password_retrieval")

    def test_changed_password_login(self):
        result_1 = self.lp.navigate_to_login_page()
        self.ast.collect_result(result_1, "Login Page Title Verification")

        self.lp.login("tester123@gmail.com", "123456")
        result_2 = self.lp.verify_valid_login()
        self.ast.collect_result(result_2, "Login Verification")

        self.ap.click_information_link()
        self.pip.change_password("123456", "1234567", "1234567")
        result_3 = self.pip.Verify_valid_password_change()
        self.ast.collect_result(result_3, "Changed Password Verification")

        result_4 = self.lp.navigate_to_login_page()
        self.ast.collect_result(result_4, "Login Page Title Verification")

        self.lp.login("tester123@gmail.com", "123456")
        result_5 = self.lp.verify_invalid_password_error_message()
        self.ast.collect_result(result_5, "Failed Login Verification")

        self.lp.login("tester123@gmail.com", "1234567")
        result_6 = self.lp.verify_valid_login()
        self.ast.collect_result(result_6, "Login Verification")

        self.ap.click_information_link()
        self.pip.change_password("1234567", "123456", "123456")
        result_7 = self.pip.Verify_valid_password_change()
        self.ast.determine_result(result_7, "Changed Password Verification",
                                  "test_changed_password_login")
