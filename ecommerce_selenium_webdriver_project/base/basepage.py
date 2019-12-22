from utilities.util import Util
from base.webdriver_setup import WebDriverSetup
from base.webdriver_wrapper import WebDriverWrapper


class BasePage(WebDriverWrapper):

    """
    Page class containing common methods that all other page classes inherit

    Should not be used to create object instances

    Arguments:
        driver(obj): Webdriver instance

    Attributes:
        main_image_num_str(str): Numeric string derived from image src property
        main_image_alt_text(str): Alternative text from image alt attribute
        driver(obj): Webdriver instance
        util(obj): Util instance
        wds(obj): Webdriver instance
        main_window(str): Main window handle
        popup_window(str): Popup window handle
    """

    # Class Attributes
    main_image_num_str = ""
    main_image_alt_text = ""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.util = Util()
        self.wds = WebDriverSetup(driver)
        self.main_window = ""
        self.popup_window = ""

    def set_main_window(self):
        """
        Assign main window handle to main_window attribute

        Parameters:
            None

        Returns:
            None
        """
        self.main_window = self.get_main_window_handle()

    def main_window_switch(self):
        """
        Switch to main window

        Parameters:
            None

        Returns:
            None
        """
        self.switch_between_windows(self.main_window)

    def popup_window_switch(self):
        """
        Switch to popup window

        Parameters:
            None

        Returns:
            None
        """
        self.popup_window = self.get_popup_window_handle()
        self.switch_between_windows(self.popup_window)

    def verify_page_title(self, text_to_verify):
        """
        Verify page title

        Parameters:
            text_to_verify(str): Text to verify in title

        Returns:
            Boolean: True for success, False for failure
        """
        try:
            title = self.get_title()
            if text_to_verify in title:
                self.log.info("Successfully verified expected text in title: "
                              + text_to_verify)
                return True
            else:
                self.log.info("Failure occured while verifying page title")
                return False
        except:
            self.log.error("Exception occured while verifying page title")
            return False

    def verify_product_discount_price(self, price_locator, price_locator_type):
        """
        Verify discount price for the selected product

        Parameters:
            price_locator(str): Locator of the price element list to find
            price_locator_type(str): Type of the locator
            (class, css, id, link, name, partial_link, tag, xpath)

        Returns:
            Boolean: True for success, False for failure
        """
        try:
            pricing_list = []
            price_info_list = self.get_element_list(price_locator,
                                                    price_locator_type)
            for price in price_info_list:
                if price.text:
                    pricing_list.append(price.text)

            discounted_price = self.util.get_numeric_string(pricing_list[0])
            percent_reduction = self.util.get_numeric_string(pricing_list[1])
            old_price = self.util.get_numeric_string(pricing_list[2])

            percent_reduction = self.util.decimal_conversion(percent_reduction)
            price_reduction = float(old_price) * percent_reduction
            new_price = float(old_price) - price_reduction

            if new_price == float(discounted_price):
                self.log.info("Successfully verified product discount price")
                return True
            else:
                self.log.info("Failure occured while verifying "
                              "product discount price")
                return False
        except:
            self.log.error("Exception occured while verifying "
                           "product discount price")
            return False

    def get_product_image_numeric_string(self, locator="",
                                         locator_type="id", element=None):
        """
        Get unique numeric string derived from the product image name

        Either provide an element or both a locator and locator_type

        Parameters:
            locator(str): Locator of the element to find, default ""
            locator_type(str): Type of the locator
            (class, css, id, link, name, partial_link, tag, xpath)
            element: Element to get product image numeric string, default None

        Returns:
            String: Derived from product image src property, default None
        """
        image_num_str = None
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            image_src_str = element.get_attribute("src")
            image_num_str = self.util.get_numeric_string(image_src_str)
            if "large" in image_src_str:
                self.log.info("Product page image "
                              "present with numeric string: " + image_num_str)
            elif "home" in image_src_str:
                self.log.info("Pop-up page image present with numeric string: "
                              + image_num_str)
            elif "small" in image_src_str:
                self.log.info("Shopping Cart page image "
                              "present with numeric string: " + image_num_str)
        except:
            self.log.error("Product image number not found")
        return image_num_str

    def verify_selected_product_thumbnail(self, image_locator,
                                          image_locator_type,
                                          thumb_locator, thumb_locator_type):
        """
        Verify the selected thumbnail matches the main product page image

        Hover above each thumbnail image to make it the main product image
        Compare the main product image numeric string to the thumbnail
        numeric string

        Parameters:
            image_locator(str): Locator of the main image element to find
            image_locator_type(str): Type of the locator
            (class, css, id, link, name, partial_link, tag, xpath)
            thumb_locator(str): Locator of the thumb image element list to find
            thumb_locator_type(str): Type of the locator
            (class, css, id, link, name, partial_link, tag, xpath)

        Returns:
            Boolean: True for success, False for failure
        """
        try:
            results = []
            main_image = self.get_element(image_locator, image_locator_type)
            thumb_list = self.get_element_list(thumb_locator,
                                               thumb_locator_type)
            for thumb in thumb_list:
                thumb_num_str = (
                    self.get_product_image_numeric_string(element=thumb))
                self.element_hover(element=thumb)
                main_image_num_str = (
                    self.get_product_image_numeric_string(element=main_image))
                if main_image_num_str == thumb_num_str:
                    results.append(True)
                else:
                    results.append(False)

            if False in results:
                self.log.info("Failure occured while verifying the selected "
                              "thumbnail matches the main product image")
                return False
            else:
                self.log.info("Successfully verified the selected thumbnail "
                              "matches the main product image")
                return True
        except:
            self.log.error("Exception occured while verifying the selected "
                           "thumbnail matches the main product image")
            return False

    def get_product_image_alt_text(self, locator, locator_type):
        """
        Get product image alternative text

        Parameters:
            locator(str): Locator of the element to find
            locator_type(str): Type of the locator
            (class, css, id, link, name, partial_link, tag, xpath)

        Returns:
            String: Alternative text from the image alt attribute, default None
        """
        image_alt_text = None
        try:
            element = self.get_element(locator, locator_type)
            image_alt_text = element.get_attribute("alt")
            self.log.info("Product image alternative text found with locator: "
                          + locator + " and locator type: " + locator_type)
        except:
            self.log.error("Cannot get product image alt text with locator: "
                           + locator + " and locator type: " + locator_type)
        return image_alt_text

    def set_main_image_alt_text(self, locator, locator_type):
        """
        Set value of main_image_alt_text with main image alt text

        Parameters:
            locator(str): Locator of the element to find
            locator_type(str): Type of the locator
            (class, css, id, link, name, partial_link, tag, xpath)

        Returns:
            None
        """
        BasePage.main_image_alt_text = (
            self.get_product_image_alt_text(locator, locator_type))

    def set_main_image_numeric_string(self, locator, locator_type):
        """
        Set value of main_image_num_str with data from main image src property

        Parameters:
            locator(str): Locator of the element to find
            locator_type(str): Type of the locator
            (class, css, id, link, name, partial_link, tag, xpath)

        Returns:
            None
        """
        BasePage.main_image_num_str = (
            self.get_product_image_numeric_string(locator, locator_type))

    def set_main_image_attributes(self, locator, locator_type):
        """
        Set value of main product page image attributes

        Parameters:
            locator(str): Locator of the element to find
            locator_type(str): Type of the locator
            (class, css, id, link, name, partial_link, tag, xpath)

        Returns:
            None
        """
        self.set_main_image_numeric_string(locator, locator_type)
        self.set_main_image_alt_text(locator, locator_type)

    def verify_product_images_match(self, locator, locator_type):
        """
        Verify image matches the main product page image

        Parameters:
            locator(str): Locator of the product page image element to find
            locator_type(str): Type of the locator
            (class, css, id, link, name, partial_link, tag, xpath)

        Returns:
            Boolean: True for success, False for failure
        """
        try:
            image_num_str = (
                self.get_product_image_numeric_string(locator, locator_type))
            image_alt_text = (
                self.get_product_image_alt_text(locator, locator_type))
            if (BasePage.main_image_num_str == image_num_str
                    and BasePage.main_image_alt_text == image_alt_text):
                self.log.info("Successfully verified product images match")
                return True
            else:
                self.log.info("Failure occured while verifying "
                              "product images match")
                return False
        except:
            self.log.error("Exception occured while verifying "
                           "product images match")
            return False

    def verify_product_review_star_rating(self, locator, locator_type,
                                          input_locator, input_locator_type):
        """
        Verify the star rating system in the review section works properly

        Parameters:
            locator(str): Locator of the star element list to find
            locator_type(str): Type of the locator
            (class, css, id, link, name, partial_link, tag, xpath)
            input_locator(str): Locator of the input element to find
            input_locator_type(str): Type of the locator
            (class, css, id, link, name, partial_link, tag, xpath)

        Returns:
            Boolean: True for success, False for failure
        """
        try:
            results = []
            star_list = self.get_element_list(locator, locator_type)
            for star in star_list[::-1]:
                star.click()
                if self.is_attribute_present(
                        input_locator, input_locator_type,
                        star.text, "value"):
                    results.append(True)
                else:
                    results.append(False)

            if False in results:
                self.log.info("Failure occured while verifying "
                              "star ratings in review section")
                return False
            else:
                self.log.info("Successfully verified star "
                              "ratings in review section")
                return True
        except:
            self.log.error("Exception occured while verifying "
                           "star ratings in review section")
            return False

    def verify_selected_product_size(self, list_locator, list_locator_type,
                                     text_locator, text_locator_type):
        """
        Verify the selected product size is correct

        Parameters:
            list_locator(str): Locator of the product size element list to find
            list_locator_type(str): Type of the locator
            (class, css, id, link, name, partial_link, tag, xpath)
            text_locator(str): Locator of the text element to find
            text_locator_type(str): Type of the locator
            (class, css, id, link, name, partial_link, tag, xpath)

        Returns:
            Boolean: True for success, False for failure
        """
        try:
            results = []
            product_size_list = (
                self.wait_for_presence_of_all_elements(list_locator,
                                                       list_locator_type))
            for size in product_size_list:
                size.click()
                text_element = (
                    self.wait_for_presence_of_element(text_locator,
                                                      text_locator_type))
                if size.text in text_element.text:
                    results.append(True)
                else:
                    results.append(False)

            if False in results:
                self.log.info("Failure occured while verifying "
                              "selected product sizes")
                return False
            else:
                self.log.info("Successfully verified selected product sizes")
                return True
        except:
            self.log.error("Exception occured while verifying "
                           "selected product size")
            return False

    def verify_selected_product_color(self, list_locator, list_locator_type,
                                      input_locator, input_locator_type):
        """
        Verify the selected product color is correct

        Parameters:
            list_locator(str): Locator of the color element list to find
            list_locator_type(str): Type of the locator
            (class, css, id, link, name, partial_link, tag, xpath)
            input_locator(str): Locator of the color input element to find
            input_locator_type(str): Type of the locator
            (class, css, id, link, name, partial_link, tag, xpath)

        Returns:
            Boolean: True for success, False for failure
        """
        try:
            results = []
            product_color_list = (
                self.wait_for_presence_of_all_elements(list_locator,
                                                       list_locator_type))
            for color in product_color_list:
                color.click()
                color_id = color.get_attribute("id")
                color_id = self.util.get_numeric_string(color_id)
                if self.is_attribute_present(
                        input_locator, input_locator_type,
                        color_id, "value"):
                    results.append(True)
                else:
                    results.append(False)

            if False in results:
                self.log.info("Failure occured while verifying "
                              "selected product colors")
                return False
            else:
                self.log.info("Successfully verified selected product colors")
                return True
        except:
            self.log.error("Exception occured while verifying "
                           "selected product color")
            return False

    def click_list_element_containing_text(self, locator,
                                           locator_type, text_to_verify):
        """
        Click list element containing given text

        Parameters:
            locator(str): Locator of the element list to find
            locator_type(str): Type of the locator
            (class, css, id, link, name, partial_link, tag, xpath)
            text_to_verify(str): Text to verify in list element

        Returns:
            None
        """
        try:
            results = []
            element_list = self.get_element_list(locator, locator_type)
            for element in element_list:
                if text_to_verify in element.text:
                    text_element = element
                    results.append(True)

            if True in results:
                self.log.info("Clicked on element with locator: "
                              + locator + " locator type: " + locator_type
                              + " and text: " + text_to_verify)
                text_element.click()
        except:
            self.log.error("Cannot click on list element with locator: "
                           + locator + " and  locator type: " + locator_type
                           + " and text: " + text_to_verify)

    def load_page_using_cookies(self, url):
        """
        load page using cookies from current session

        Parameters:
            url(str): Address to navigate to

        Returns:
            None
        """
        try:
            cookies = self.driver.get_cookies()
            self.driver = self.wds.get_webdriver_instance()
            self.driver.get(url)
            for cookie in cookies:
                if "expiry" in cookie:
                    del cookie["expiry"]
                self.driver.add_cookie(cookie)

            self.refresh_page()
            self.log.info(
                "Page loaded successfully using cookies and URL: " + url)
        except:
            self.log.error(
                "Page loaded unsuccessfully using cookies and URL: " + url)

    def scroll_page(self, locator, locator_type):
        try:
            element = self.wait_for_presence_of_element(locator, locator_type)
            self.driver.execute_script(
                "arguments[0].scrollIntoView(true);", element)
            self.log.info("Page scrolled to element with locator: "
                          + locator + " locator type: " + locator_type)
        except:
            self.log.error("Exception occured while scrolling to element")
