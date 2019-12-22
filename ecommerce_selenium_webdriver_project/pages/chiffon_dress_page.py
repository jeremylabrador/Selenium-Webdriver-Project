import logging
from base.basepage import BasePage
from utilities.custom_logger import custom_logger


class ChiffonDressPage(BasePage):

    """
    Page class representing the chiffon dress product page

    Contains methods that interact with web elements
    located on the chiffon dress product page

    Arguments:
        None

    Attributes:
        log(obj): Custom logger object
    """

    log = custom_logger(logging.INFO)

    # locators
    _dress_size = "#uniform-group_1 > span"
    _size_menu_list = "#group_1 option"
    _color_selected = "#color_to_pick_list a"
    _input_color = "div.attribute_list > input.color_pick_hidden"
    _submit_button = "Submit"
    _twitter_button = "button.btn-twitter"
    _facebook_button = "button.btn-facebook"
    _google_button = "button.btn-google-plus"
    _pinterest_button = "button.btn-pinterest"
    _item_name = "h1"
    _product_model = "product_reference"
    _product_condition = "product_condition"
    _product_description = "short_description_content"
    _review_link = "ul.comments_advices a.open-comment-form"
    _review_popup = "div.fancybox-wrap"
    _review_close = "a.fancybox-close"
    _review_button = "new_comment_tab_btn"
    _review_ok_button = "div.fancybox-inner p.submit > button"
    _review_send_button = "submitNewMessage"
    _review_error_message = "#new_comment_form_error ul"
    _review_star_ratings = "div.star_content a"
    _review_star_rating_value = "div.star_content > input"
    _review_title_input = "comment_title"
    _review_comment_input = "content"
    _review_success_message = "div.fancybox-inner > p:nth-child(2)"
    _email_link = "send_friend_button"
    _email_name_input = "friend_name"
    _email_address_input = "friend_email"
    _email_send_button = "sendEmail"
    _email_error_message = "send_friend_form_error"
    _email_success_message = "div.fancybox-inner > p:nth-child(2)"
    _email_ok_button = "p.submit input.button"
    _print_link = "li.print > a"
    _wishlist_link = "wishlist_button"
    _wishlist_success_message = "div.fancybox-wrap"
    _wishlist_close_link = "a.fancybox-close"
    _main_image = "bigpic"
    _data_sheet = "table.table-data-sheet"
    _brand_info = "section.page-product-box div.rte > p"
    _null_error_message = "div.fancybox-inner > p.fancybox-error"
    _dress_quantity_input = "quantity_wanted"
    _close_null_error_message = "a.fancybox-close"
    _dress_quantity_value = "quantity_wanted"
    _review_cancel_link = "div.fancybox-inner a.closefb"
    _email_cancel_link = "p.submit > a.closefb"
    _thumb_list = "li a img"
    _price_info_list = "div.price p"
    _size_menu = "#group_1 [value='3']"
    _color_pick = "color_15"
    _product_page_image = "bigpic"
    _delete_cart_item = "span.remove_link > a.ajax_cart_block_remove_link"
    _hover_shopping_cart = "div.shopping_cart > a"
    _empty_cart_quantity = "div.shopping_cart a > span.ajax_cart_no_product"
    _popup_cart_product_image = "div.product-image-container > img"
    _popup_cart_message = "div.layer_cart_product > h2"
    _popup_cart_product_title = "layer_cart_product_title"
    _popup_cart_product_attributes = "layer_cart_product_attributes"
    _popup_cart_product_quantity = "layer_cart_product_quantity"
    _popup_cart_product_price = "layer_cart_product_price"
    _popup_cart_quantity_text = "h2 span.ajax_cart_product_txt"
    _popup_cart_total = "div.layer_cart_row > span.ajax_block_cart_total"
    _popup_cart_continue_button = "div.button-container > span.continue"
    _popup_cart_checkout_button = "div.button-container > a.button"
    _popup_cart_products_total = (
        "div.layer_cart_row > span.ajax_block_products_total")
    _popup_cart_shipping_cost = (
        "div.layer_cart_row > span.ajax_cart_shipping_cost")

    def verify_chiffon_dress_page_title(self):
        return self.wait_for_title("Printed Chiffon Dress - My Store")

    def set_chiffon_dress_main_window_attribute(self):
        self.set_main_window()

    def click_chiffon_dress_twitter_button(self):
        element = self.wait_for_element_to_be_clickable(
            self._twitter_button, "css")
        self.click_element(element=element)

    def click_chiffon_dress_facebook_button(self):
        element = self.wait_for_element_to_be_clickable(
            self._facebook_button, "css")
        self.click_element(element=element)

    def click_chiffon_dress_google_button(self):
        element = self.wait_for_element_to_be_clickable(
            self._google_button, "css")
        self.click_element(element=element)

    def click_chiffon_dress_pinterest_button(self):
        element = self.wait_for_element_to_be_clickable(
            self._pinterest_button, "css")
        self.click_element(element=element)

    def chiffon_dress_popup_window_switch(self):
        self.popup_window_switch()

    def verify_chiffon_dress_popup_url(self, text_to_verify):
        return self.wait_for_url(text_to_verify)

    def chiffon_dress_main_window_switch(self):
        self.main_window_switch()

    def verify_social_media_button(self, text_to_verify):
        self.chiffon_dress_popup_window_switch()
        result = self.verify_chiffon_dress_popup_url(text_to_verify)
        self.chiffon_dress_main_window_switch()
        return result

    def verify_chiffon_dress_item_name(self):
        return self.is_text_present(self._item_name, "css",
                                    "Printed Chiffon Dress")

    def verify_chiffon_dress_product_model(self):
        return self.is_text_present(self._product_model,
                                    "id", "Model demo_7")

    def verify_chiffon_dress_product_condition(self):
        return self.is_text_present(self._product_condition,
                                    "id", "Condition New")

    def verify_chiffon_dress_product_description(self):
        return self.is_text_present(self._product_description, "id",
                                    "Printed chiffon knee length dress "
                                    "with tank straps. Deep v-neckline.")

    def verify_chiffon_dress_data_sheet(self):
        return self.is_text_present(self._data_sheet, "css",
                                    "Compositions Polyester", "Styles Girly",
                                    "Properties Midi Dress", selector="tr")

    def verify_chiffon_dress_brand_info(self):
        return self.is_text_present(self._brand_info, "css",
                                    "Fashion has been creating well-designed "
                                    "collections since 2010. The brand offers "
                                    "feminine designs delivering stylish "
                                    "separates and statement dresses which "
                                    "has since evolved into a full "
                                    "ready-to-wear collection in which every "
                                    "item is a vital part of a woman's "
                                    "wardrobe. The result? Cool, easy, chic "
                                    "looks with youthful elegance and "
                                    "unmistakable signature style. All the "
                                    "beautiful pieces are made in Italy and "
                                    "manufactured with the greatest "
                                    "attention. Now Fashion extends to a "
                                    "range of accessories including shoes, "
                                    "hats, belts and more!")

    def click_chiffon_dress_review_link(self):
        element = self.wait_for_element_to_be_clickable(
            self._review_link, "css")
        self.click_element(element=element)

    def verify_chiffon_dress_review_popup(self):
        return self.is_element_present(self._review_popup, "css")

    def click_chiffon_dress_review_close(self):
        element = self.wait_for_element_to_be_clickable(
            self._review_close, "css")
        self.click_element(element=element)

    def click_chiffon_dress_review_button(self):
        element = self.wait_for_element_to_be_clickable(
            self._review_button, "id")
        self.click_element(element=element)

    def enter_review_title_input(self, title_comment):
        self.sending_keys(title_comment, self._review_title_input)

    def enter_review_comment_input(self, comment):
        self.sending_keys(comment, self._review_comment_input)

    def click_chiffon_dress_review_send_button(self):
        element = self.wait_for_element_to_be_clickable(
            self._review_send_button, "id")
        self.click_element(element=element)

    def enter_chiffon_dress_review_info(self, title_comment="Dress Review",
                                        comment="Fantastic dress!"):
        self.enter_review_title_input(title_comment)
        self.enter_review_comment_input(comment)
        self.click_chiffon_dress_review_send_button()

    def verify_chiffon_dress_review_error_message(self, *args):
        return self.is_text_present(self._review_error_message,
                                    "css", *args, selector="li")

    def click_chiffon_dress_review_cancel_link(self):
        element = self.wait_for_element_to_be_clickable(
            self._review_cancel_link, "css")
        self.click_element(element=element)

    def click_chiffon_dress_review_star_rating(self):
        return self.verify_product_review_star_rating(
            self._review_star_ratings, "css",
            self._review_star_rating_value, "css")

    def verify_chiffon_dress_review_success_message(self):
        return self.is_text_present(self._review_success_message, "css",
                                    "Your comment has been added and will be "
                                    "available once approved by a moderator")

    def click_chiffon_dress_review_ok_button(self):
        element = self.wait_for_element_to_be_clickable(
            self._review_ok_button, "css")
        self.click_element(element=element)

    def click_chiffon_dress_email_link(self):
        element = self.wait_for_element_to_be_clickable(self._email_link, "id")
        self.click_element(element=element)

    def enter_chiffon_dress_email_name_input(self, email_name):
        self.sending_keys(email_name, self._email_name_input)

    def enter_chiffon_dress_email_address_input(self, email_address):
        self.sending_keys(email_address, self._email_address_input)

    def click_chiffon_dress_email_send_button(self):
        element = self.wait_for_element_to_be_clickable(
            self._email_send_button, "id")
        self.click_element(element=element)

    def enter_chiffon_dress_email_info(self, email_name="Alan Smithee",
                                       email_address="AlanSmithee@gmail.com"):
        self.enter_chiffon_dress_email_name_input(email_name)
        self.enter_chiffon_dress_email_address_input(email_address)
        self.click_chiffon_dress_email_send_button()

    def verify_chiffon_dress_email_error_message(self):
        return self.is_text_present(self._email_error_message, "id",
                                    "You did not fill required fields")

    def click_chiffon_dress_email_cancel_link(self):
        element = self.wait_for_element_to_be_clickable(
            self._email_cancel_link, "css")
        self.click_element(element=element)

    def verify_chiffon_dress_email_success_message(self):
        return self.is_text_present(self._email_success_message, "css",
                                    "Your e-mail has been sent successfully")

    def click_chiffon_dress_email_ok_button(self):
        element = self.wait_for_element_to_be_clickable(
            self._email_ok_button, "css")
        self.click_element(element=element)

    def verify_chiffon_dress_print_link(self):
        return self.is_attribute_present(self._print_link, "css",
                                         "javascript:print();", "href")

    def click_chiffon_dress_wishlist_link(self):
        element = self.wait_for_element_to_be_clickable(
            self._wishlist_link, "id")
        self.click_element(element=element)

    def verify_chiffon_dress_wishlist_success_message(self):
        return self.is_text_present(self._wishlist_success_message,
                                    "css", "Added to your wishlist.")

    def click_chiffon_dress_wishlist_close_link(self):
        element = self.wait_for_element_to_be_clickable(
            self._wishlist_close_link, "css")
        self.click_element(element=element)

    def scroll_to_chiffon_dress_thumbnails(self):
        self.scroll_page(self._main_image, "id")

    def verify_selected_chiffon_dress_thumbnail(self):
        return self.verify_selected_product_thumbnail(self._main_image, "id",
                                                      self._thumb_list, "css")

    def verify_chiffon_dress_discount_price(self):
        return self.verify_product_discount_price(self._price_info_list, "css")

    def verify_chiffon_dress_quantity(self):
        return self.is_attribute_present(self._dress_quantity_value,
                                         "id", "1", "value")

    def enter_chiffon_dress_quantity(self, quantity):
        self.sending_keys(quantity, self._dress_quantity_input)

    def click_chiffon_dress_submit_button(self):
        element = self.wait_for_element_to_be_clickable(
            self._submit_button, "name")
        self.click_element(element=element)

    def verify_chiffon_dress_null_error_message(self):
        return self.is_text_present(self._null_error_message,
                                    "css", "Null quantity.")

    def close_chiffon_dress_null_error_message(self):
        element = self.wait_for_element_to_be_clickable(
            self._close_null_error_message, "css")
        self.click_element(element=element)

    def verify_chiffon_dress_quantity_error_message(self, quantity):
        self.enter_chiffon_dress_quantity(quantity)
        self.click_chiffon_dress_submit_button()
        result = self.verify_chiffon_dress_null_error_message()
        self.close_chiffon_dress_null_error_message()
        return result

    def verify_selected_chiffon_dress_size(self):
        return self.verify_selected_product_size(self._size_menu_list, "css",
                                                 self._dress_size, "css")

    def verify_selected_chiffon_dress_color(self):
        return self.verify_selected_product_color(self._color_selected, "css",
                                                  self._input_color, "css")

    def select_chiffon_dress_size(self):
        element = self.wait_for_element_to_be_clickable(self._size_menu, "css")
        self.click_element(element=element)

    def select_chiffon_dress_color(self):
        element = self.wait_for_element_to_be_clickable(self._color_pick, "id")
        self.click_element(element=element)

    def order_chiffon_dress(self):
        self.select_chiffon_dress_size()
        self.select_chiffon_dress_color()
        self.click_chiffon_dress_submit_button()

    def verify_chiffon_dress_popup_cart_success_message(self):
        return self.wait_for_element_text(self._popup_cart_message, "css",
                                          "Product successfully added to "
                                          "your shopping cart")

    def verify_chiffon_dress_popup_cart_product_image(self):
        return self.verify_product_images_match(self._popup_cart_product_image,
                                                "css")

    def verify_chiffon_dress_popup_cart_product_title(self):
        return self.is_text_present(self._popup_cart_product_title,
                                    "id", "Printed Chiffon Dress")

    def verify_chiffon_dress_popup_cart_product_attributes(self):
        return self.is_text_present(self._popup_cart_product_attributes,
                                    "id", "Green, L")

    def verify_chiffon_dress_popup_cart_product_quantity(self):
        return self.is_text_present(self._popup_cart_product_quantity,
                                    "id", "1")

    def verify_chiffon_dress_popup_cart_product_price(self):
        return self.is_text_present(self._popup_cart_product_price,
                                    "id", "$16.40")

    def verify_chiffon_dress_popup_cart_quantity_text(self):
        return self.is_text_present(self._popup_cart_quantity_text,
                                    "css", "There is 1 item in your cart.")

    def verify_chiffon_dress_popup_cart_products_total(self):
        return self.is_text_present(self._popup_cart_products_total,
                                    "css", "$16.40")

    def verify_chiffon_dress_popup_cart_shipping_cost(self):
        return self.is_text_present(self._popup_cart_shipping_cost,
                                    "css", "$2.00")

    def verify_chiffon_dress_popup_cart_total(self):
        return self.is_text_present(self._popup_cart_total,
                                    "css", "$18.40")

    def click_chiffon_dress_popup_continue_button(self):
        element = self.wait_for_element_to_be_clickable(
            self._popup_cart_continue_button, "css")
        self.click_element(element=element)

    def scroll_to_chiffon_dress_menu_cart(self):
        self.scroll_page(self._hover_shopping_cart, "css")

    def chiffon_dress_menu_cart_hover(self):
        self.element_hover(self._hover_shopping_cart, "css")

    def click_chiffon_dress_remove_link(self):
        element = self.wait_for_element_to_be_clickable(
            self._delete_cart_item, "css")
        self.click_element(element=element)

    def verify_chiffon_dress_empty_cart_quantity(self):
        return self.wait_for_element_text(self._empty_cart_quantity,
                                          "css", "(empty)")

    def set_chiffon_dress_image_attributes(self):
        self.set_main_image_attributes(self._product_page_image, "id")

    def click_chiffon_dress_popup_cart_checkout_button(self):
        element = self.wait_for_element_to_be_clickable(
            self._popup_cart_checkout_button, "css")
        self.click_element(element=element)
