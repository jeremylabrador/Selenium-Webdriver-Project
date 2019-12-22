import logging
from utilities.custom_logger import custom_logger


class AssertStatus():

    """
    Collects assert results from multiple verification points in one test case

    After collecting the result of the final verification point
    the status of a test case will be determined

    Arguments:
        None

    Attributes:
        log(obj): Logger instance
        result_list(list): Holds True or False results
    """

    log = custom_logger(logging.INFO)

    def __init__(self):
        self.result_list = []

    def collect_result(self, result, result_message):
        """
        Appends True or False to the result list depending on the result

        Parameters:
            result(bool): True or False assert result
            result_message(str): Message describing the verification point

        Returns:
            None
        """
        try:
            if result is not None:
                if result:
                    self.result_list.append(True)
                    self.log.info("VERIFICATION SUCCESSFUL: " + result_message)
                else:
                    self.result_list.append(False)
                    self.log.error("VERIFICATION FAILED: " + result_message)
            else:
                self.result_list.append(False)
                self.log.error("VERIFICATION FAILED: " + result_message)
        except:
            self.result_list.append(False)
            self.log.error("Exception occured while determining result")

    def determine_result(self, result, result_message, test_name):
        """
        Collects the result of the final verification point in a test case

        Parameters:
            result(bool): True or False assert result
            result_message(str): Message describing the verification point
            test_name(str): Name of current test

        Returns:
            None
        """
        self.collect_result(result, result_message)

        if False in self.result_list:
            self.log.error("TEST FAILED: " + test_name)
            assert False
        else:
            self.log.info("TEST SUCCESSFUL: " + test_name)
            assert True
