import pytest
from utilities.assert_status import AssertStatus
from pages.chiffon_dress_page import ChiffonDressPage
from pages.dresses_page import DressesPage
from utilities.read_csv_data import get_csv_data
from pages.shopping_cart_page import ShoppingCartPage


@pytest.mark.usefixtures("one_time_setup", "setup")
class TestShoppingCart():

    @pytest.fixture(autouse=True)
    def object_setup(self):
        self.dp = DressesPage(self.driver)
        self.cdp = ChiffonDressPage(self.driver)
        self.scp = ShoppingCartPage(self.driver)
        self.scp_session = ShoppingCartPage(self.driver)
        self.ast = AssertStatus()

    def test_chiffon_dress_shopping_cart_details(self):
        result_1 = self.dp.navigate_to_dresses_page()
        self.ast.collect_result(result_1, "Dresses Page Title Verification")

        self.dp.click_chiffon_dress_link()
        result_2 = self.cdp.verify_chiffon_dress_page_title()
        self.ast.collect_result(
            result_2, "Chiffon Dress Page Title Verification")

        self.cdp.order_chiffon_dress()
        self.cdp.set_chiffon_dress_image_attributes()
        self.cdp.click_chiffon_dress_popup_cart_checkout_button()
        result_3 = self.scp.verify_shopping_cart_page_title()
        self.ast.collect_result(
            result_3, "Shopping Cart Page Title Verification")

        result_4 = self.scp.verify_chiffon_dress_product_image()
        self.ast.collect_result(result_4, "Chiffon Dress Image Verification")

        result_5 = self.scp.verify_chiffon_dress_product_title()
        self.ast.collect_result(
            result_5, "Chiffon Dress Product Title Verification")

        result_6 = self.scp.verify_chiffon_dress_product_model()
        self.ast.collect_result(
            result_6, "Chiffon Dress Product Model Verification")

        result_7 = self.scp.verify_chiffon_dress_product_attributes()
        self.ast.collect_result(
            result_7, "Chiffon Dress Product Attributes Verification")

        result_8 = self.scp.verify_chiffon_dress_discount_price()
        self.ast.collect_result(
            result_8, "Chiffon Dress Discount Price Verification")

        self.scp.click_delete_chiffon_dress()
        result_9 = self.scp.verify_empty_shopping_cart()
        self.ast.determine_result(result_9, "Empty Shopping Cart Verification",
                                  "test_chiffon_dress_shopping_cart_details")

    @pytest.mark.parametrize(
        "update_quantity, quantity, price, products_total, "
        "shipping, subtotal, tax, total, delete_quantity",
        get_csv_data("product_totals_test_data.csv"))
    def test_chiffon_dress_shopping_cart_product_totals(
            self, update_quantity, quantity, price, products_total,
            shipping, subtotal, tax, total, delete_quantity):
        result_1 = self.dp.navigate_to_dresses_page()
        self.ast.collect_result(result_1, "Dresses Page Title Verification")

        self.dp.click_chiffon_dress_link()
        result_2 = self.cdp.verify_chiffon_dress_page_title()
        self.ast.collect_result(
            result_2, "Chiffon Dress Page Title Verification")

        self.cdp.order_chiffon_dress()
        self.cdp.click_chiffon_dress_popup_cart_checkout_button()
        result_3 = self.scp.verify_shopping_cart_page_title()
        self.ast.collect_result(
            result_3, "Shopping Cart Page Title Verification")

        self.scp.enter_chiffon_dress_quantity(update_quantity)
        result_9 = self.scp.verify_chiffon_dress_quantity(quantity)
        self.ast.collect_result(
            result_9, "Chiffon Dress Quantity Verification")

        result_10 = self.scp.verify_chiffon_dress_total_product_price(price)
        self.ast.collect_result(
            result_10, "Chiffon Dress Product Price Verification")

        result_11 = (
            self.scp.verify_shopping_cart_products_total(products_total))
        self.ast.collect_result(
            result_11, "Shopping Cart Products Total Verification")

        result_12 = self.scp.verify_shopping_cart_shipping_total(shipping)
        self.ast.collect_result(
            result_12, "Shopping Cart Shipping Total Verification")

        result_13 = self.scp.verify_shopping_cart_subtotal(subtotal)
        self.ast.collect_result(
            result_13, "Shopping Cart Subtotal Verification")

        result_14 = self.scp.verify_shopping_cart_tax_total(tax)
        self.ast.collect_result(
            result_14, "Shopping Cart Tax Total Verification")

        result_15 = self.scp.verify_shopping_cart_price_total(total)
        self.ast.collect_result(
            result_15, "Shopping Cart Price Total Verification")

        self.scp.enter_chiffon_dress_quantity(delete_quantity)
        result_16 = self.scp.verify_empty_shopping_cart()
        self.ast.determine_result(
            result_16, "Empty Shopping Cart Verification",
            "test_chiffon_dress_shopping_cart_product_totals")

    def test_loading_chiffon_dress_shopping_cart_session(self):
        result_1 = self.dp.navigate_to_dresses_page()
        self.ast.collect_result(result_1, "Dresses Page Title Verification")

        self.dp.click_chiffon_dress_link()
        result_2 = self.cdp.verify_chiffon_dress_page_title()
        self.ast.collect_result(
            result_2, "Chiffon Dress Page Title Verification")

        self.cdp.order_chiffon_dress()
        self.cdp.click_chiffon_dress_popup_cart_checkout_button()
        result_3 = self.scp.verify_shopping_cart_page_title()
        self.ast.collect_result(
            result_3, "Shopping Cart Page Title Verification")

        self.scp_session.load_shopping_cart_session()
        result_4 = self.scp_session.verify_chiffon_dress_product_title()
        self.ast.collect_result(
            result_4, "Chiffon Dress Product Title Verification")

        self.scp_session.click_delete_chiffon_dress()
        result_5 = self.scp_session.verify_empty_shopping_cart()
        self.ast.collect_result(result_5, "Empty Shopping Cart Verification")

        self.scp_session.quit_shopping_cart_page()
        self.scp.refresh_shopping_cart_page()
        result_6 = self.scp.verify_empty_shopping_cart()
        self.ast.determine_result(
            result_6, "Empty Shopping Cart Verification",
            "test_loading_chiffon_dress_shopping_cart_session")
