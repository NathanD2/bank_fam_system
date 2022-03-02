import abc


class UserType(abc.ABC):
    """
    Create the User Type abstract class.
    """
    def __init__(self):
        """
        Initialization of lockout.
        """
        self._lockout = False

    @property
    def lockout(self):
        """
        Get lockout.
        :return: boolean
        """
        return self._lockout

    @lockout.setter
    def lockout(self, lockout):
        """
        Set Lockout.
        :param lockout: boolean
        """
        self._lockout = lockout

    @abc.abstractmethod
    def warning_exceed(self, amount_left, amount_alloc):
        """
        Create warning_exceed abstractmethod.
        :param amount_left: float
        :param amount_alloc: float
        """
        pass

    @abc.abstractmethod
    def notified_exceed(self, amount_left, amount_alloc):
        """
        Create notified_exceed abstractmethod.
        :param amount_left: float
        :param amount_alloc: float
        """
        pass

    @abc.abstractmethod
    def lockout_check(self):
        """
        Create lockout_check abstractmethod.
        """
        pass

    @abc.abstractmethod
    def __str__(self):
        """
        Create tostring abstractmethod.
        """
        pass
