import pytest
from utilities.assert_status import AssertStatus
from pages.chiffon_dress_page import ChiffonDressPage
from pages.dresses_page import DressesPage
from utilities.read_csv_data import get_csv_data


@pytest.mark.usefixtures("one_time_setup", "setup")
class TestProductDetailPage():

    @pytest.fixture(autouse=True)
    def setup_class(self):
        self.dp = DressesPage(self.driver)
        self.cdp = ChiffonDressPage(self.driver)
        self.ast = AssertStatus()

    def test_chiffon_dress_social_media_buttons(self):
        result_1 = self.dp.navigate_to_dresses_page()
        self.ast.collect_result(result_1, "Dresses Page Title Verification")

        self.dp.click_chiffon_dress_link()
        result_2 = self.cdp.verify_chiffon_dress_page_title()
        self.ast.collect_result(
            result_2, "Chiffon Dress Page Title Verification")

        self.cdp.set_chiffon_dress_main_window_attribute()

        self.cdp.click_chiffon_dress_twitter_button()
        result_3 = self.cdp.verify_social_media_button("twitter.com")
        self.ast.collect_result(result_3, "Twitter Button Verification")

        self.cdp.click_chiffon_dress_facebook_button()
        result_4 = self.cdp.verify_social_media_button("facebook.com")
        self.ast.collect_result(result_4, "Facebook Button Verification")

        self.cdp.click_chiffon_dress_google_button()
        result_5 = self.cdp.verify_social_media_button("google.com")
        self.ast.collect_result(result_5, "Google Button Verification")

        self.cdp.click_chiffon_dress_pinterest_button()
        result_6 = self.cdp.verify_social_media_button("pinterest.com")
        self.ast.determine_result(result_6, "Pinterest Button Verification",
                                  "test_chiffon_dress_social_media_buttons")

    def test_chiffon_dress_product_info(self):
        result_1 = self.dp.navigate_to_dresses_page()
        self.ast.collect_result(result_1, "Dresses Page Title Verification")

        self.dp.click_chiffon_dress_link()
        result_2 = self.cdp.verify_chiffon_dress_page_title()
        self.ast.collect_result(
            result_2, "Chiffon Dress Page Title Verification")

        result_3 = self.cdp.verify_chiffon_dress_item_name()
        self.ast.collect_result(result_3, "Item Name Verification")

        result_4 = self.cdp.verify_chiffon_dress_product_model()
        self.ast.collect_result(result_4, "Product Model Verification")

        result_5 = self.cdp.verify_chiffon_dress_product_condition()
        self.ast.collect_result(result_5, "Product Condition Verification")

        result_6 = self.cdp.verify_chiffon_dress_product_description()
        self.ast.collect_result(result_6, "Product Description Verification")

        result_7 = self.cdp.verify_chiffon_dress_data_sheet()
        self.ast.collect_result(result_7, "Data Sheet Verification")

        result_8 = self.cdp.verify_chiffon_dress_brand_info()
        self.ast.determine_result(result_8, "Dress Brand Info Verification",
                                  "test_chiffon_dress_product_info")

    def test_chiffon_dress_review_link(self):
        result_1 = self.dp.navigate_to_dresses_page()
        self.ast.collect_result(result_1, "Dresses Page Title Verification")

        self.dp.click_chiffon_dress_link()
        result_2 = self.cdp.verify_chiffon_dress_page_title()
        self.ast.collect_result(
            result_2, "Chiffon Dress Page Title Verification")

        self.cdp.click_chiffon_dress_review_link()
        result_3 = self.cdp.verify_chiffon_dress_review_popup()
        self.ast.determine_result(result_3, "Review Pop-up Verification",
                                  "test_chiffon_dress_review_link")
        self.cdp.click_chiffon_dress_review_cancel_link()

    @pytest.mark.parametrize(
        "title, comment, title_error_message, comment_error_message",
        get_csv_data("review_test_data.csv"))
    def test_invalid_chiffon_dress_review(
            self, title, comment, title_error_message, comment_error_message):
        result_1 = self.dp.navigate_to_dresses_page()
        self.ast.collect_result(result_1, "Dresses Page Title Verification")

        self.dp.click_chiffon_dress_link()
        result_2 = self.cdp.verify_chiffon_dress_page_title()
        self.ast.collect_result(
            result_2, "Chiffon Dress Page Title Verification")

        self.cdp.click_chiffon_dress_review_button()
        self.cdp.enter_chiffon_dress_review_info(title, comment)
        result_3 = (self.cdp.verify_chiffon_dress_review_error_message(
            title_error_message, comment_error_message))
        self.ast.determine_result(
            result_3, "Review Error Messages Verification",
            "test_invalid_chiffon_dress_review")
        self.cdp.click_chiffon_dress_review_cancel_link()

    def test_valid_chiffon_dress_review(self):
        result_1 = self.dp.navigate_to_dresses_page()
        self.ast.collect_result(result_1, "Dresses Page Title Verification")

        self.dp.click_chiffon_dress_link()
        result_2 = self.cdp.verify_chiffon_dress_page_title()
        self.ast.collect_result(
            result_2, "Chiffon Dress Page Title Verification")

        self.cdp.click_chiffon_dress_review_button()
        result_3 = self.cdp.click_chiffon_dress_review_star_rating()
        self.ast.collect_result(result_3, "Review Star Ratings Verification")

        self.cdp.enter_chiffon_dress_review_info()
        result_4 = self.cdp.verify_chiffon_dress_review_success_message()
        self.ast.determine_result(
            result_4, "Review Success Message Verification",
            "test_valid_chiffon_dress_review")
        self.cdp.click_chiffon_dress_review_ok_button()

    @pytest.mark.parametrize(
        "email_name, email_address", get_csv_data("email_test_data.csv"))
    def test_invalid_chiffon_dress_email(self, email_name, email_address):
        result_1 = self.dp.navigate_to_dresses_page()
        self.ast.collect_result(result_1, "Dresses Page Title Verification")

        self.dp.click_chiffon_dress_link()
        result_2 = self.cdp.verify_chiffon_dress_page_title()
        self.ast.collect_result(
            result_2, "Chiffon Dress Page Title Verification")

        self.cdp.click_chiffon_dress_email_link()
        self.cdp.enter_chiffon_dress_email_info(email_name, email_address)
        result_3 = self.cdp.verify_chiffon_dress_email_error_message()
        self.ast.determine_result(result_3, "Email Error Message Verification",
                                  "test_invalid_chiffon_dress_email")
        self.cdp.click_chiffon_dress_email_cancel_link()

    def test_valid_chiffon_dress_email(self):
        result_1 = self.dp.navigate_to_dresses_page()
        self.ast.collect_result(result_1, "Dresses Page Title Verification")

        self.dp.click_chiffon_dress_link()
        result_2 = self.cdp.verify_chiffon_dress_page_title()
        self.ast.collect_result(
            result_2, "Chiffon Dress Page Title Verification")

        self.cdp.click_chiffon_dress_email_link()
        self.cdp.enter_chiffon_dress_email_info()
        result_3 = self.cdp.verify_chiffon_dress_email_success_message()
        self.ast.determine_result(
            result_3, "Email Succes Message Verification",
            "test_valid_chiffon_dress_email")
        self.cdp.click_chiffon_dress_email_ok_button()

    def test_chiffon_dress_print_section(self):
        result_1 = self.dp.navigate_to_dresses_page()
        self.ast.collect_result(result_1, "Dresses Page Title Verification")

        self.dp.click_chiffon_dress_link()
        result_2 = self.cdp.verify_chiffon_dress_page_title()
        self.ast.collect_result(
            result_2, "Chiffon Dress Page Title Verification")

        result_3 = self.cdp.verify_chiffon_dress_print_link()
        self.ast.determine_result(result_3, "Print Link Verification",
                                  "test_chiffon_dress_print_section")

    def test_chiffon_dress_wishlist_section(self):
        result_1 = self.dp.navigate_to_dresses_page()
        self.ast.collect_result(result_1, "Dresses Page Title Verification")

        self.dp.click_chiffon_dress_link()
        result_2 = self.cdp.verify_chiffon_dress_page_title()
        self.ast.collect_result(
            result_2, "Chiffon Dress Page Title Verification")

        self.cdp.click_chiffon_dress_wishlist_link()
        result_3 = self.cdp.verify_chiffon_dress_wishlist_success_message()
        self.ast.determine_result(
            result_3, "Wishlist Success Message Verification",
            "test_chiffon_dress_wishlist_section")
        self.cdp.click_chiffon_dress_wishlist_close_link()

    def test_chiffon_dress_image_selection(self):
        result_1 = self.dp.navigate_to_dresses_page()
        self.ast.collect_result(result_1, "Dresses Page Title Verification")

        self.dp.click_chiffon_dress_link()
        result_2 = self.cdp.verify_chiffon_dress_page_title()
        self.ast.collect_result(
            result_2, "Chiffon Dress Page Title Verification")

        self.cdp.scroll_to_chiffon_dress_thumbnails()

        result_3 = self.cdp.verify_selected_chiffon_dress_thumbnail()
        self.ast.determine_result(result_3, "Image Match Verification",
                                  "test_chiffon_dress_image_section")

    def test_chiffon_dress_product_details(self):
        result_1 = self.dp.navigate_to_dresses_page()
        self.ast.collect_result(result_1, "Dresses Page Title Verification")

        self.dp.click_chiffon_dress_link()
        result_2 = self.cdp.verify_chiffon_dress_page_title()
        self.ast.collect_result(
            result_2, "Chiffon Dress Page Title Verification")

        result_3 = self.cdp.verify_chiffon_dress_discount_price()
        self.ast.collect_result(result_3, "Dress Discount Price Verification")

        result_4 = self.cdp.verify_chiffon_dress_quantity()
        self.ast.collect_result(
            result_4, "Chiffon Dress Quantity Value Verification")

        result_5 = self.cdp.verify_selected_chiffon_dress_size()
        self.ast.collect_result(
            result_5, "Chiffon Dress Selected Size Verification")

        result_6 = self.cdp.verify_selected_chiffon_dress_color()
        self.ast.collect_result(
            result_6, "Chiffon Dress Selected Color Verification")

        result_7 = self.cdp.verify_chiffon_dress_quantity_error_message("a")
        self.ast.determine_result(
            result_7, "Chiffon Dress Quantity Error Message Verification",
            "test_chiffon_dress_product_details")

    def test_chiffon_dress_popup_cart_details(self):
        result_1 = self.dp.navigate_to_dresses_page()
        self.ast.collect_result(result_1, "Dresses Page Title Verification")

        self.dp.click_chiffon_dress_link()
        result_2 = self.cdp.verify_chiffon_dress_page_title()
        self.ast.collect_result(
            result_2, "Chiffon Dress Page Title Verification")

        self.cdp.order_chiffon_dress()
        self.cdp.set_chiffon_dress_image_attributes()
        result_3 = self.cdp.verify_chiffon_dress_popup_cart_success_message()
        self.ast.collect_result(
            result_3, "Chiffon Dress Pop-up Cart Success Message Verification")

        result_4 = self.cdp.verify_chiffon_dress_popup_cart_product_image()
        self.ast.collect_result(
            result_4, "Chiffon Dress Pop-up Cart Image Verification")

        result_5 = self.cdp.verify_chiffon_dress_popup_cart_product_title()
        self.ast.collect_result(
            result_5, "Chiffon Dress Pop-up Cart Product Title Verification")

        result_6 = (
            self.cdp.verify_chiffon_dress_popup_cart_product_attributes())
        self.ast.collect_result(
            result_6,
            "Chiffon Dress Pop-up Cart Product Attributes Verification")

        result_7 = self.cdp.verify_chiffon_dress_popup_cart_product_quantity()
        self.ast.collect_result(
            result_7,
            "Chiffon Dress Pop-up Cart Product Quantity Verification")

        result_8 = self.cdp.verify_chiffon_dress_popup_cart_product_price()
        self.ast.collect_result(
            result_8, "Chiffon Dress Pop-up Cart Product Price Verification")

        result_9 = self.cdp.verify_chiffon_dress_popup_cart_quantity_text()
        self.ast.collect_result(
            result_9, "Chiffon Dress Pop-up Cart Quantity Text Verification")

        result_10 = self.cdp.verify_chiffon_dress_popup_cart_products_total()
        self.ast.collect_result(
            result_10, "Chiffon Dress Pop-up Cart Products Total Verification")

        result_11 = self.cdp.verify_chiffon_dress_popup_cart_shipping_cost()
        self.ast.collect_result(
            result_11, "Chiffon Dress Pop-up Cart Shipping Cost Verification")

        result_12 = self.cdp.verify_chiffon_dress_popup_cart_total()
        self.ast.collect_result(
            result_12, "Chiffon Dress Pop-up Cart Total Verification")

        self.cdp.click_chiffon_dress_popup_continue_button()
        self.cdp.scroll_to_chiffon_dress_menu_cart()
        self.cdp.chiffon_dress_menu_cart_hover()
        self.cdp.click_chiffon_dress_remove_link()
        result_13 = self.cdp.verify_chiffon_dress_empty_cart_quantity()
        self.ast.determine_result(
            result_13, "Chiffon Dress Empty Cart Quantity Verification",
            "test_chiffon_dress_popup_cart_details")
