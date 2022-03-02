"""
Module represents a bank account class.
"""


class BankAccount:
    """
    Represents a bank account.
    """

    def __init__(self, balance, bank_name, bank_num):
        """
        Initializes a bank account.
        :param balance: a float
        :param bank_name: a string
        :param bank_num: a string
        """
        self._balance = balance
        self._bank_name = bank_name
        self._bank_num = bank_num

    def set_balance(self, new_bal):
        """
        Sets balance.
        :param new_bal: a float
        :return:
        """
        self._balance = new_bal

    def get_balance(self):
        """
        Gets balance.
        :return: a float
        """
        return self._balance

    def set_bank_name(self, name):
        """
        Sets bank name.
        :param name: a string
        :return:
        """
        self._bank_name = name

    def get_bank_name(self):
        """
        Gets bank name.
        :return: a string
        """
        return self._bank_name

    def set_bank_num(self, bank_num):
        """
        Sets bank number.
        :param bank_num: a string
        :return:
        """
        self._bank_num = bank_num

    def get_bank_num(self):
        """
        Gets bank number.
        :return: a string
        """
        return self._bank_num

    def reduce_balance(self, amount):
        """
        Reduces bank balance by amount.
        :param amount: a float
        :return:
        """
        self.set_balance(self.get_balance() - amount)

    def __str__(self):
        """
        Returns string representation of bank account.
        :return: a string
        """
        return f"Bank Name: {self.get_bank_name()}\n" \
               f"Bank Number: {self.get_bank_num()}"\
            f"\nBalance: {self.get_balance()}\n"
