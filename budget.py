"""
Module represents Budget Categories.
"""
import enum
from enum import auto


class BudgetCategory(enum.Enum):
    """
    Create an enum to work on BudgetCategory
    """
    GamesAndEntertainment = auto()
    ClothingAndAccessories = auto()
    Food = auto()
    Miscellaneous = auto()


class Budget:
    """
    Create a budget class to handle the transactions by category
    """

    def __init__(self, _amount_alloc, user_input):
        """
        Initializes a budget.
        :param _amount_alloc: a float
        :param user_input: an int
        """
        self._transactions = list()
        self._amount_spent = 0
        self._amount_left = _amount_alloc
        self._amount_alloc = _amount_alloc
        self._budgetCategory = BudgetCategory(user_input)
        self._is_exceeded = False

    @property
    def transactions(self):
        """
        Get transactions.
        :return: a list
        """
        return self._transactions

    @property
    def amount_spend(self):
        """
        Get amount spend.
        :return: a float
        """
        return self._amount_spent

    @amount_spend.setter
    def amount_spend(self, amount_spent):
        """
        Set amount spend.
        :param amount_spent:
        """
        self._amount_spent = amount_spent

    @property
    def amount_left(self):
        """
        Get amount left.
        :return: a float
        """
        return self._amount_left

    @amount_left.setter
    def amount_left(self, amount_left):
        """
        Set amount left
        :param amount_left: a float
        """
        self._amount_left = amount_left

    @property
    def amount_alloc(self):
        """
        Gets amount_alloc.
        :return: a float
        """
        return self._amount_alloc

    @property
    def is_exceeded(self):
        """
        Returns is_exceeded value.
        :return: a boolean
        """
        return self._is_exceeded

    @is_exceeded.setter
    def is_exceeded(self, new_state):
        """
        Sets is_exceeded.
        :param new_state: a boolean
        :return:
        """
        self._is_exceeded = new_state

    def add_transaction(self, transaction):
        """
        Add a transaction in the transactions.
        :param transaction: Transaction object
        """
        self._transactions.append(transaction)

    def view_transactions(self):
        """
        View transaction by category.
        """
        count = 0
        for element in self._transactions:
            count += 1
            print(f"Transaction {count}------------------------")
            print(element)

    def get_cate(self):
        """
        Gets budget category.
        :return: a String
        """
        return f"Budget Category: {self._budgetCategory.name}"

    def __str__(self):
        """
        Display the info of budget.
        :return: a string
        """
        return f"Budget Category: {self._budgetCategory.name}\n" \
               f"Amount Left: {self.amount_left}\n" \
               f"----------------------------------\n"
