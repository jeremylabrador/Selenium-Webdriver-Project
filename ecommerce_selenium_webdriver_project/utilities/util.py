import logging
import re
from utilities.custom_logger import custom_logger


class Util():

    """
    Methods that help with common tasks

    Arguments:
        None

    Attributes:
        log: Logger instance
    """

    log = custom_logger(logging.INFO)

    def get_numeric_string(self, str):
        """
        Get numeric string from a given string

        Parameters:
            str(str): String used to get a numeric string

        Returns:
            String: A string of numbers
            Only the last string in the findall list will be returned
        """
        try:
            return re.findall(r'(\d+\.?\d*)', str)[-1]
        except:
            self.log.error("Failed to get numeric string")

    def decimal_conversion(self, num_str):
        """
        Convert a percentage to a decimal

        Parameters:
            num_str(str): Numeric string to be converted to a decimal

        Returns:
            Float: Decimal
        """
        try:
            return float(num_str)/100
        except:
            self.log.error("Failed to get decimal")
