from user_type import UserType


class Troublemaker(UserType):
    """
    Create an troublemaker class which is a subclass for UserType with different conditions.
    """

    def __init__(self):
        """
        Initialize the self._warning_threshold as 0.75.
        """
        super().__init__()
        self._warning_threshold = 0.75

    def notified_exceed(self, amount_left, amount_alloc):
        """
        Notified exceed if the expense exceed by 100%. If the expense exceed by 120% of and set lockout true.
        :param amount_left: float
        :param amount_alloc: float
        :return: boolean
        """
        if -amount_alloc * 0.2 > amount_left:
            print("You exceed it by 120% of the amount assigned to the budget.\nLock out this budget.")
            self.lockout = True
        elif amount_left < 0:
            print("\nYou have exceeded a budget category.")

        return self.lockout

    def warning_exceed(self, amount_left, amount_alloc):
        """
        Give a warning if a user spend money more than 75%.
        :param amount_left: float
        :param amount_alloc: float
        """
        if amount_left / amount_alloc < 1 - self._warning_threshold:
            print("\nYou have exceeded more than 75% of a budget category.")

    def lockout_check(self):
        """
        Lock check set as false.
        :return: boolean
        """
        return False

    def __str__(self):
        """
        Display Troublemaker class.
        :return: string
        """
        return "Troublemaker"
