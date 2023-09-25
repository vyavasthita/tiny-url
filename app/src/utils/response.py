#! /usr/bin/python3.10

"""Response module.

@file response.py
@author Dilip Kumar Sharma
@date 21st Sept 2023

About; -
--------
    This python module is responsible for creating response object.

Uses; -
-------
    To generate response.

Reference; -
------------
    TBD
"""

# import statements in alphabetical order
# python and third party lib import statements come first before our own class/method imports


class Response:
    """ To generate response.

    This class is used to generate response.

    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
    """
    def __init__(self, is_error=False, is_success=False, status_code=0, error_code=0, result=None, message=str(), error=str()):
        """ Response object

        This class is used to generate response.

        Args:
            is_success: True if response is a success otherwise False.
            status_code: Integer value used for value of status.
            result: Value which we would like to return. It could be any python data type.
            message: Human readable/custom message.
            error: Error message read from handling exception.
        Returns:
            Not Applicable.
        Raises:
            Not Applicable.
        """
        self.is_error = is_error
        self.is_success = is_success
        self.status_code = status_code
        self.error_code = error_code
        self.result = result
        self.message = message
        self.error = error
