from user_type import UserType


class Angel(UserType):
    """
    Create an angel class which is a subclass for UserType with different conditions.
    """
    def __init__(self):
        """
        Initialize the self._warning_threshold as 0.0.
        """
        super().__init__()
        self._warning_threshold = 0.9

    def notified_exceed(self, amount_left, amount_alloc=0):
        """
        Notified exceed if the amount left blew zero and set lockout false.
        :param amount_left: float
        :param amount_alloc: float
        :return: boolean
        """
        if amount_left < 0:
            print("\nPardon the intrusion, but you have exceed your budget.")
        return self.lockout

    def warning_exceed(self, amount_left, amount_alloc):
        """
        Give a warning if a user spend money more than 90%.
        :param amount_left: float
        :param amount_alloc: float
        """
        if amount_left / amount_alloc < 1 - self._warning_threshold:
            print("\nYou exceed more than 90% of a budget category.")

    def lockout_check(self):
        """
        Lock check set as false.
        :return: boolean
        """
        return False

    def __str__(self):
        """
        Display Angel class.
        :return: string
        """
        return "Angel"
