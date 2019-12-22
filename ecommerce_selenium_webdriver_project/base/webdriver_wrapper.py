from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class WebDriverWrapper():

    """
    Class containing Selenium WebDriver methods wrapped into custom methods

    The WebDriverWrapper class is inherited by the Basepage class
    and should not be used to create object instances

    Arguments:
        driver(obj): Webdriver instance

    Attributes:
        driver(obj): Webdriver instance
    """

    def __init__(self, driver):
        self.driver = driver
        self.by = By()

    def get_title(self):
        """
        Get the title of the current page

        Parameters:
            None

        Returns:
            String: Title of the current webpage
        """
        return self.driver.title

    def get_by_type(self, locator_type):
        """
        Get "By" type of the provided locator type

        Parameters:
            locator_type(str): Type of the locator
            (class, css, id, link, name, partial_link, tag, xpath)

        Returns:
            "By" type
        """
        try:
            results = []
            by_list = []
            for item in dir(self.by):
                by_list.append(item.lower())

            for item in by_list:
                if locator_type in item and "__" not in item:
                    results.append(item)

            locator_type = min(results, key=len)
            locator_type = locator_type.upper()
            locator_type = getattr(self.by, locator_type)
            return locator_type
        except:
            self.log.error("Locator type is incorrect: " + locator_type)
            return False

    def sending_keys(self, data, locator, locator_type="id"):
        """
        Send keys to element

        Parameters:
            data(str): A string to fill out form fields
            locator(str): locator of the element to find
            locator_type(str): Type of the locator, default id
            (class, css, id, link, name, partial_link, tag, xpath)

        Returns:
            None
        """
        try:
            element = self.get_element(locator, locator_type)
            element.clear()
            element.send_keys(data)
            self.log.info("Sending keys to element with locator: "
                          + locator + " and locator type: " + locator_type)
        except:
            self.log.error("Cannot send keys to element with locator: "
                           + locator + " and locator type: " + locator_type)

    def is_element_present(self, locator, locator_type="id"):
        """
        Check if element is present

        Parameters:
            locator(str): Locator of the element to check
            locator_type(str): Type of the locator, default id
            (class, css, id, link, name, partial_link, tag, xpath)

        Returns:
            Boolean: True for success, False for failure
        """
        try:
            if self.get_element(locator, locator_type):
                self.log.info("Element present with locator: "
                              + locator + " and locator type: " + locator_type)
                return True
            else:
                self.log.info("Element not present with locator: "
                              + locator + " and locator type: " + locator_type)
                return False
        except:
            self.log.error("Element not present with locator: "
                           + locator + " and locator type: " + locator_type)
            return False

    def get_by_category_type(self, category_type):
        """
        Get a number returned representing a category type

        Parameters:
            category_type(str): Clothing category type
            (tops, t-shirts, blouses, dresses, casual dresses,
             evening dresses, summer dresses)

        Returns:
            Integer
        """
        category_type = category_type.lower()
        if category_type == "tops":
            return 0
        elif category_type == "t-shirts":
            return 1
        elif category_type == "blouses":
            return 2
        elif category_type == "dresses":
            return 3
        elif category_type == "casual dresses":
            return 4
        elif category_type == "evening dresses":
            return 5
        elif category_type == "summer dresses":
            return 6
        else:
            self.log.error("Category type is incorrect: " + category_type)
        return False

    def get_element(self, locator, locator_type="id"):
        """
        Get element for the provided locator and locator type

        Parameters:
            locator(str): locator of the element to find
            locator_type(str): Type of the locator, default id
            (class, css, id, link, name, partial_link, tag, xpath)

        Returns:
            Element, default None
        """
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info("Element found with locator: "
                          + locator + " and locator type: " + locator_type)
        except:
            self.log.error("Element not found with locator: "
                           + locator + " and locator type: " + locator_type)
        return element

    def click_element(self, locator="", locator_type="id", element=None):
        """
        Click element

        Parameters:
            locator(str): locator of the element to click
            locator_type(str): Type of the locator, default id
            (class, css, id, link, name, partial_link, tag, xpath)
            element: Element to click on, default None

        Returns:
            None
        """
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.click()
            if locator:
                self.log.info("Clicked on element successfully with locator: "
                              + locator + " and locator type: " + locator_type)
            else:
                self.log.info("Clicked on element successfully")
        except:
            self.log.error("Cannot click on element with locator: "
                           + locator + " and locator type: " + locator_type)

    def configure_category_type_element(self, locator, category_type):
        """
        Configures an element for a javascript script

        Parameters:
            locator(str): locator of the element to find
            category_type(str): Type of the clothing category
            (tops, t-shirts, blouses, dresses, casual dresses,
             evening dresses, summer dresses)

        Returns:
            Element, default None
        """
        element = None
        try:
            category_type_num = self.get_by_category_type(category_type)
            element = "$('{}')[{}]".format(locator, category_type_num)
            self.log.info("Element configured successfully with locator: "
                          + locator + " and category type: " + category_type)
        except:
            self.log.error("Element not configured successfully with locator: "
                           + locator + " and category type: " + category_type)
        return element

    def click_category_type_element(self, locator, category_type):
        """
        Click category type element

        Parameters:
            locator(str): locator of the element to find
            category_type(str): Type of the clothing category
            (tops, t-shirts, blouses, dresses, casual dresses,
             evening dresses, summer dresses)

        Returns:
            None
        """
        try:
            element = self.configure_category_type_element(locator,
                                                           category_type)
            result = self.wait_for_presence_of_all_elements(locator, "css")
            if result is not None:
                element = element + ".click()"
                self.driver.execute_script(element)
                self.log.info("Clicked on element with locator: "
                              + locator + " and category type: "
                              + category_type)
            else:
                self.log.info("Cannot click on element with locator: "
                              + locator + " and category type: "
                              + category_type)
        except:
            self.log.error("Cannot click on element with locator: "
                           + locator + " and category type: " + category_type)

    def is_text_present(self, locator, locator_type, *args, selector="li"):
        """
        Check if text is present

        Parameters:
            locator(str): Locator of the element to find
            locator_type(str): Type of the locator
            (class, css, id, link, name, partial_link, tag, xpath)
            *args(str): Text to check if present
            selector: Used for multiple list item text, default li

        Returns:
            Boolean: True for success, False for failure
        """
        try:
            text_to_verify = " ".join(args)
            actual_text = self.get_element(locator, locator_type)
            if len(args) >= 2:
                actual_texts = (
                    actual_text.find_elements_by_css_selector(selector))
                for item in actual_texts:
                    if item.text in text_to_verify:
                        self.log.info("Text present with locator: "
                                      + locator + " and locator type: "
                                      + locator_type)
                        return True
                    else:
                        self.log.info("Text not present with locator: "
                                      + locator + " and locator type: "
                                      + locator_type)
                        return False
            else:
                if text_to_verify in actual_text.text:
                    self.log.info("Text present with locator: "
                                  + locator + " and locator type: "
                                  + locator_type)
                    return True
                else:
                    self.log.info("Text not present with locator: "
                                  + locator + " and locator type: "
                                  + locator_type)
                    return False
        except:
            self.log.error("Exception occured while verifying if text present")
            return False

    def is_attribute_present(self, locator, locator_type,
                             text_to_verify, attribute):
        """
        Check if given text is present in attribute's value

        Parameters:
            locator(str): Locator of the element to find
            locator_type(str): Type of the locator
            (class, css, id, link, name, partial_link, tag, xpath)
            text_to_verify(str): Text to verify in attribute
            attribute(str): Attribute to verify for text

        Returns:
            Boolean: True for success, False for failure
        """
        try:
            element = self.get_element(locator, locator_type)
            if text_to_verify in element.get_attribute(attribute):
                self.log.info("Attribute present with locator: "
                              + locator + " and locator type: " + locator_type)
                return True
            else:
                self.log.info("Attribute not present with locator: "
                              + locator + " and locator type: " + locator_type)
                return False
        except:
            self.log.error("Exception occured while verifying "
                           "if attribute present")
            return False

    def close_window(self):
        """
        Close current browser window

        Parameters:
            None

        Returns:
            None
        """
        self.driver.close()

    def get_main_window_handle(self):
        """
        Get main window handle

        Parameters:
            None

        Returns:
            Main window handle
        """
        return self.driver.window_handles[0]

    def get_popup_window_handle(self):
        """
        Get popup window handle

        Parameters:
            None

        Returns:
            Popup window handle
        """
        return self.driver.window_handles[1]

    def switch_between_windows(self, window_choice):
        """
        Switch between windows

        Parameters:
            window_choice(str): window to switch to

        Returns:
            None
        """
        self.driver.switch_to.window(window_choice)

    def get_current_url(self):
        """
        Get the URL of the current page

        Parameters:
            None

        Returns:
            URL of the current page(str)
        """
        return self.driver.current_url

    def verify_url_text(self, text_to_verify):
        """
        Verify text is in URL

        Parameters:
            text_to_verify(str): Text to verify in URL

        Returns:
            Boolean: True for success, False for failure
        """
        try:
            url = self.get_current_url()
            self.close_window()
            if text_to_verify in url:
                self.log.info(text_to_verify + " present in URL")
                return True
            else:
                self.log.info(text_to_verify + " not present in URL")
                return False
        except:
            self.log.error(text_to_verify + " not present in URL")
            return False

    def get_element_list(self, locator, locator_type="id"):
        """
        Get list of elements

        Parameters:
            locator(str): Locator of the element to find
            locator_type(str): Type of the locator, default id
            (class, css, id, link, name, partial_link, tag, xpath)

        Returns:
             List of elements, default None
        """
        elements = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            elements = self.driver.find_elements(by_type, locator)
            self.log.info("Element list found with locator: "
                          + locator + " and locator type: " + locator_type)
        except:
            self.log.info("Element list not found with locator: "
                          + locator + " and locator type: " + locator_type)
        return elements

    def element_hover(self, locator="", locator_type="id", element=None):
        """
        Hover over element
        Either provide an element or both a locator and locator_type

        Parameters:
            locator(str): Locator of the element to hover over
            locator_type(str): Type of the locator, default id
            (class, css, id, link, name, partial_link, tag, xpath)
            element: Element to hover over, default None

        Returns:
            None
        """
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()
            if locator:
                self.log.info("Hover successful with locator: "
                              + locator + " and locator type: " + locator_type)
            else:
                self.log.info("Hover successful with element")
        except:
            self.log.error("Cannot hover on element with locator: "
                           + locator + " and locator type: " + locator_type)

    def refresh_page(self):
        """
        Refresh the current page

        Parameters:
            None

        Returns:
            None
        """
        self.driver.refresh()

    def quit_window(self):
        """
        Quits the driver and closes every associated window

        Parameters:
            None

        Returns:
            None
        """
        self.driver.quit()

    def wait_for_element_text(self, locator, locator_type, text_to_verify):
        """
        Explicit Wait checking for the given text in an element

        Parameters:
            locator(str): Locator of the element to find
            locator_type(str): Type of the locator
            (class, css, id, link, name, partial_link, tag, xpath)
            text_to_verify(str): Text to verify in element

        Returns:
            Boolean: True for success, False for failure, default False
        """
        result = False
        try:
            by_type = self.get_by_type(locator_type)
            self.log.info("Waiting up to 10 seconds for "
                          "text to be present in element")
            wait = WebDriverWait(self.driver, 10)
            result = wait.until(
                EC.text_to_be_present_in_element((by_type, locator),
                                                 text_to_verify))
            self.log.info("Text present in element with locator: "
                          + locator + " and locator type: " + locator_type)
        except:
            self.log.error("Exception occured while verifying "
                           "if text present in element")
        return result

    def wait_for_element_value_text(self, locator,
                                    locator_type, text_to_verify):
        """
        Explicit Wait checking for the given text in an element's value

        Parameters:
            locator(str): Locator of the element to find
            locator_type(str): Type of the locator
            (class, css, id, link, name, partial_link, tag, xpath)
            text_to_verify(str): Text to verify in element's value

        Returns:
            Boolean: True for success, False for failure, default False
        """
        result = False
        try:
            by_type = self.get_by_type(locator_type)
            self.log.info("Waiting up to 10 seconds for "
                          "text to be present in element's value")
            wait = WebDriverWait(self.driver, 10)
            result = wait.until(
                EC.text_to_be_present_in_element_value((by_type, locator),
                                                       text_to_verify))
            self.log.info("Text present in element value with locator: "
                          + locator + " and locator type: " + locator_type)
        except:
            self.log.error("Exception occured while verifying "
                           "if text present in element value")
        return result

    def wait_for_title(self, text_to_verify):
        """
        Explicit Wait checking for the given text in a page title

        Parameters:
            text_to_verify(str): Text to verify in a page title

        Returns:
            Boolean: True for success, False for failure, default False
        """
        result = False
        try:
            self.log.info("Waiting up to 10 seconds for "
                          "expected text to be present in title")
            wait = WebDriverWait(self.driver, 10)
            result = wait.until(EC.title_contains(text_to_verify))
            self.log.info("Successfully verified expected text in title: "
                          + text_to_verify)
        except:
            self.log.error("Exception occured while verifying "
                           "if text present in title")
        return result

    def wait_for_presence_of_element(self, locator, locator_type):
        """
        Explicit Wait checking that an element is present

        Parameters:
            locator(str): Locator of the element to find
            locator_type(str): Type of the locator
            (class, css, id, link, name, partial_link, tag, xpath)

        Returns:
            Element, default None
        """
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            self.log.info("Waiting up to 10 seconds for "
                          "the presence of the element to be located")
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(
                EC.presence_of_element_located((by_type, locator)))
            self.log.info("Element present with locator: "
                          + locator + " and locator type: " + locator_type)
        except:
            self.log.error("Element not present with locator: "
                           + locator + " and locator type: " + locator_type)
        return element

    def wait_for_presence_of_all_elements(self, locator, locator_type):
        """
        Explicit Wait checking that all elements are present

        Parameters:
            locator(str): Locator of the element to find
            locator_type(str): Type of the locator
            (class, css, id, link, name, partial_link, tag, xpath)

        Returns:
            List of elements, default None
        """
        elements = None
        try:
            by_type = self.get_by_type(locator_type)
            self.log.info("Waiting up to 10 seconds for "
                          "the presence of all elements to be located")
            wait = WebDriverWait(self.driver, 10)
            elements = wait.until(
                EC.presence_of_all_elements_located((by_type, locator)))
            self.log.info("Elements present with locator: "
                          + locator + " and locator type: " + locator_type)
        except:
            self.log.error("Elements not present with locator: "
                           + locator + " and locator type: " + locator_type)
        return elements

    def wait_for_element_to_be_clickable(self, locator, locator_type):
        """
        Explicit Wait checking if element is visible and enabled to click

        Parameters:
            locator(str): Locator of the element to find
            locator_type(str): Type of the locator
            (class, css, id, link, name, partial_link, tag, xpath)

        Returns:
            Element, default None
        """
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            self.log.info("Waiting up to 10 seconds for "
                          "element to be clickable")
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(
                EC.element_to_be_clickable((by_type, locator)))
            self.log.info("Clicked on element successfully with locator: "
                          + locator + " and locator type: " + locator_type)
        except:
            self.log.error("Cannot click on element with locator: "
                           + locator + " and locator type: " + locator_type)
        return element

    def wait_for_url(self, url):
        """
        Explicit Wait checking for the given text in the current url

        Parameters:
            url(str): Text to verify in the current url

        Returns:
            Boolean: True for success, False for failure, default False
        """
        result = False
        try:
            self.log.info("Waiting up to 10 seconds for "
                          "expected text to be present in url")
            wait = WebDriverWait(self.driver, 10)
            result = wait.until(EC.url_contains((url)))
            self.close_window()
            self.log.info(url + " present in URL")
        except:
            self.log.error(url + " not present in URL")
        return result
