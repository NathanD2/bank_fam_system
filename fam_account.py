"""
This module represents a Fam Account class.
"""
from transaction import Transaction

# Category constants.
GAMES_AND_ENTERTAINMENT = '1'
CLOTHING_AND_ACCESSORIES = '2'
FOOD = '3'
MISC = '4'


class FamAccount:
    """
    Represents a FAM account.
    """

    def __init__(self, user, bank_account, budgets):
        """
        Initializes a FAM account.
        :param user: a User
        :param bank_account: a BankAccount
        :param budgets: a dict
        """
        self._user = user
        self._bank_account = bank_account
        self._budgets = budgets

    def get_user(self):
        """
        Gets user.
        :return: a User
        """
        return self._user

    def get_bank_account(self):
        """
        Gets bank account.
        :return: a BankAccount
        """
        return self._bank_account

    @property
    def budgets(self):
        """
        Gets budget.
        :return: a dict
        """
        return self._budgets

    @budgets.setter
    def budgets(self, budgets):
        """
        Sets budgets.
        :param budgets: a dict
        :return:
        """
        self._budgets = budgets

    def display_account_details(self):
        """
        Displays account details.
        :return:
        """
        print(self.get_user())

    @staticmethod
    def print_budget_categories():
        """
        Prints budget categories.
        :return:
        """
        print("Budget Categories:\n"
              "1. Games And Entertainment\n"
              "2. Clothing And Accessories\n"
              "3. Food\n"
              "4. Miscellaneous")

    def select_budget_cat(self):
        """
        Prompts the user to select a Budget category.
        :return: a BudgetCategory String
        """
        while True:
            self.print_budget_categories()
            budget_choice = input("Enter budget category choice: ")
            if budget_choice == GAMES_AND_ENTERTAINMENT:
                budget_cat = "GamesAndEntertainment"
                return budget_cat
            elif budget_choice == CLOTHING_AND_ACCESSORIES:
                budget_cat = "ClothingAndAccessories"
                return budget_cat
            elif budget_choice == FOOD:
                budget_cat = "Food"
                return budget_cat
            elif budget_choice == MISC:
                budget_cat = "Miscellaneous"
                return budget_cat
            else:
                print("Invalid Input.\n")
                continue

    def create_new_transaction(self):
        """
        Creates a new transaction for a budget.

        Alters BankAccount balance and adds the new transaction to a Budget's
        transaction list.
        :return:
        """
        amount = float(input("Enter amount: "))
        origin = input("Transaction Origin: ")
        budget = self.find_budget()

        if self._bank_account.get_balance() - amount < 0:
            print(f"You cannot make a transaction for ${amount}.\n")
            return False

        # Restricts transactions if budget category is exceeded.
        if budget.is_exceeded:
            print(f"{budget.get_cate()} is lockout.\n")
            # return
        else:
            transaction = Transaction(amount, origin)
            budget.add_transaction(transaction)
            budget.amount_spend += amount
            budget.amount_left -= amount
            bank_account = self.get_bank_account()
            bank_account.set_balance(bank_account.get_balance() - amount)
            budget_amount_left = budget.amount_left
            budget_amount_alloc = budget.amount_alloc
            if self.get_user().get_notified_exceeded(budget_amount_left, budget_amount_alloc):
                budget.is_exceeded = True
            else:
                self.get_user().get_warning_exceed(budget_amount_left, budget_amount_alloc)
                print("add it successfully!\n")

        # Check is_exceeded after transaction, whether needed to be changed.
        if self.get_user().get_lockout_check():
            print("All categories are lockout\n")
            return True
        else:
            return False

    def find_budget(self):
        """
        Finds a budget.
        :return: a Budget
        """
        budget_cat = self.select_budget_cat()  # User selected category.
        return self._budgets[budget_cat]

    def display_transaction_details(self):
        """
        Displays transactions' details for a budget.
        :return:
        """
        budget_cat = self.select_budget_cat()
        budget = self._budgets[budget_cat]
        print(budget)
        budget.view_transactions()

    def __str__(self):
        """
        Returns a string representation of a FamAccount.
        :return: a string.
        """
        return f"{self.get_user()}" \
               f"Bank Account Information: \n{self.get_bank_account()}"
