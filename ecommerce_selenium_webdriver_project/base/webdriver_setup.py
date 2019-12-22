from selenium import webdriver


class WebDriverSetup():

    """
    Creates a webdriver instance based on chosen browser

    Arguments:
        browser(str): Browser to use

    Attributes:
        browser(str): Browser to use
    """

    def __init__(self, browser):
        self.browser = browser

    def get_webdriver_instance(self):
        """
        Get webdriver instance based on the chosen browser

        Parameters:
            None

        Returns:
            Webdriver instance
        """
        if self.browser == "chrome":
            driver = webdriver.Chrome()
            print("Running tests on Chrome")
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
            print("Running tests on Firefox")
        else:
            driver = webdriver.Chrome()
            print("Running tests on Chrome")

        base_URL = "http://automationpractice.com/index.php"
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(base_URL)

        return driver
