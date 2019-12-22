import logging
from base.basepage import BasePage
from utilities.custom_logger import custom_logger


class ShoppingCartPage(BasePage):

    """
    Page class representing the shopping cart page

    Contains methods that interact with web elements
    located on the shopping cart page

    Arguments:
        None

    Attributes:
        log: Custom logger object
    """

    log = custom_logger(logging.INFO)

    # locators
    _shopping_cart_image = "tbody tr:nth-child(1) td.cart_product a > img"
    _price_info_list = "td.cart_unit span > span"
    _total_product_price = "tbody tr:nth-child(1) td.cart_total > span"
    _products_total = "total_product"
    _shipping_total = "total_shipping"
    _subtotal = "total_price_without_tax"
    _tax_total = "total_tax"
    _price_total = "total_price"
    _empty_cart = "p.alert-warning"
    _product_model = "small.cart_ref"
    _quantity_input = (
        "td.cart_quantity.text-center > input.cart_quantity_input")
    _shopping_cart_product_title = (
        "tbody tr:nth-child(1) td.cart_description p.product-name > a")
    _shopping_cart_product_attributes = (
        "tbody tr:nth-child(1) td.cart_description small > a")
    _delete_chiffon_dress = (
        "tbody tr:nth-child(1) td.cart_delete div > a.cart_quantity_delete")
    _chiffon_dress_quantity = (
        "tbody tr:nth-child(1) td.cart_quantity.text-center "
        "> input:nth-child(1)")

    def verify_shopping_cart_page_title(self):
        return self.verify_page_title("Order - My Store")

    def verify_chiffon_dress_product_image(self):
        return self.verify_product_images_match(self._shopping_cart_image,
                                                "css")

    def verify_chiffon_dress_product_title(self):
        return self.is_text_present(self._shopping_cart_product_title,
                                    "css", "Printed Chiffon Dress")

    def verify_chiffon_dress_product_model(self):
        return self.is_text_present(self._product_model, "css", "SKU : demo_7")

    def verify_chiffon_dress_product_attributes(self):
        return self.is_text_present(self._shopping_cart_product_attributes,
                                    "css", "Color : Green, Size : L")

    def verify_chiffon_dress_discount_price(self):
        return self.verify_product_discount_price(self._price_info_list, "css")

    def click_delete_chiffon_dress(self):
        self.click_element(self._delete_chiffon_dress, "css")

    def verify_empty_shopping_cart(self):
        return self.wait_for_element_text(self._empty_cart, "css",
                                          "Your shopping cart is empty.")

    def enter_chiffon_dress_quantity(self, quantity):
        self.sending_keys(quantity, self._quantity_input, "css")

    def verify_chiffon_dress_quantity(self, text_to_verify):
        return self.wait_for_element_value_text(self._chiffon_dress_quantity,
                                                "css", text_to_verify)

    def verify_chiffon_dress_total_product_price(self, text_to_verify):
        return self.is_text_present(self._total_product_price, "css",
                                    text_to_verify)

    def verify_shopping_cart_products_total(self, text_to_verify):
        return self.is_text_present(self._products_total, "id", text_to_verify)

    def verify_shopping_cart_shipping_total(self, text_to_verify):
        return self.is_text_present(self._shipping_total, "id", text_to_verify)

    def verify_shopping_cart_subtotal(self, text_to_verify):
        return self.is_text_present(self._subtotal, "id", text_to_verify)

    def verify_shopping_cart_tax_total(self, text_to_verify):
        return self.is_text_present(self._tax_total, "id", text_to_verify)

    def verify_shopping_cart_price_total(self, text_to_verify):
        return self.is_text_present(self._price_total, "id", text_to_verify)

    def load_shopping_cart_session(self):
        self.load_page_using_cookies(
            "http://automationpractice.com/index.php?controller=order")

    def quit_shopping_cart_page(self):
        self.quit_window()

    def refresh_shopping_cart_page(self):
        self.refresh_page()
