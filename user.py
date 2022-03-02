"""
This module represents a transaction class.
"""


class User:
    def __init__(self, username, age, user_type):
        """
        Initializes a User.
        :param username: a string
        :param age: an int
        :param user_type: a UserType
        """
        self._username = username
        self._age = age
        self._user_type = user_type

    @property
    def username(self):
        """
        Gets/sets the username.
        :return:
        """
        return self._username

    @property
    def age(self):
        """
        Gets/sets the age.
        :return:
        """
        return self._age

    @property
    def user_type(self):
        """
        Gets/sets the UserType
        :return:
        """
        return self._user_type

    def get_warning_exceed(self, budget_amount_left, budget_amount_alloc):
        """
        Gets warning_exceed from userType.
        :param budget_amount_left: float
        :param budget_amount_alloc: float
        """
        self.user_type.warning_exceed(budget_amount_left, budget_amount_alloc)

    def get_notified_exceeded(self, budget_amount_left, budget_amount_alloc):
        """
        Gets notified_exceeded from userType.
        :param budget_amount_left: float
        :param budget_amount_alloc: float
        """
        return self.user_type.notified_exceed(budget_amount_left, budget_amount_alloc)

    def get_lockout_check(self):
        """
        Gets lockout_check from userType.
        """
        return self.user_type.lockout_check()


    def __str__(self):
        """
        Returns string representation of the User.
        :return:
        """
        return f"-----User Name: {self.username} ----\n" \
               f"Age: {self.age} \n" \
               f"User Type: {self.user_type} \n" \
