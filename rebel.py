from user_type import UserType


class Rebel(UserType):
    """
    Create a rebel class which is a subclass for UserType with different conditions.
    """

    def __init__(self):
        """
        Initialize the self._warning_threshold as 0.5, budgets_exceeded_limit is 2 and
        lockout_count to count the lockout budgets.
        """
        super().__init__()
        self._warning_threshold = 0.5
        self._budgets_exceeded_limit = 2
        self._lockout_count = 0

    def notified_exceed(self, amount_left, amount_alloc=0):
        """
        Notified exceed if the expense exceed by 100% , set lockout true and count the lockout numbers.
        :param amount_left: float
        :param amount_alloc: float
        :return: boolean
        """
        if amount_left < 0:
            print("\nYOU HAVE EXCEEDED A BUDGET CATEGORY!!! STOP SPENDING MONEY!!!")
            self.lockout = True
            self._lockout_count += 1
        return self.lockout

    def warning_exceed(self, amount_left, amount_alloc):
        """
        Give a warning if a user spend money more than 50%.
        :param amount_left: float
        :param amount_alloc: float
        """
        if amount_left / amount_alloc < 1 - self._warning_threshold:
            print("\nYou exceed more than 50% of a budget category.")

    def lockout_check(self):
        """
        If the lockout_count is equal or larger than budgets_exceeded_limit then return true. Otherwise, return false.
        :return:
        """
        if self._lockout_count >= self._budgets_exceeded_limit:
            return True
        else:
            return False

    def __str__(self):
        """
        Display Rebel class.
        :return: string
        """
        return "Rebel"
