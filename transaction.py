"""
This module represents a Transaction class.
"""
import datetime
import time


class Transaction:
    """
    Represents a Transaction.
    """

    def __init__(self, amount, origin):
        """
        Initializes a Transaction.
        :param amount: a float
        :param origin: a string
        """
        self._datetime = datetime.datetime.fromtimestamp(time.time())
        self._amount = amount
        self._origin = origin

    def get_datetime(self):
        """
        Gets the datetime.
        :return: a datetime object
        """
        return self._datetime

    def get_amount(self):
        """
        Gets amount.
        :return: a float
        """
        return self._amount

    @property
    def amount(self):
        """
        Gets amount.
        :return: a float
        """
        return self._amount

    @property
    def origin(self):
        """
        Gets origin.
        :return: a string
        """
        return self._origin

    def __str__(self):
        """
        Returns string representation of a Transaction.
        :return:
        """
        return f"Date: {self.get_datetime().strftime('%Y-%m-%d %H:%M:%S')}\n" \
               f"Amount: {self.get_amount()}\n" \
               f"Purchase Origin: {self.origin}\n"
