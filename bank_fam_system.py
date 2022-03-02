"""
Module represents a Bank FAM System class.
"""
from fam_account import FamAccount
from bank_account import BankAccount
from budget import Budget
from angel import Angel
from troublemaker import Troublemaker
from rebel import Rebel
from user import User
from budget import BudgetCategory


class BankFamSystem:
    """
    Represents a Bank FAM System.
    """

    def __init__(self):
        """
        Initializes a bank FAM system.
        """
        self._fam_accounts = []

    @property
    def fam_accounts(self):
        """
        Gets list of FAM accounts.
        :return: a list of FamAccounts
        """
        return self._fam_accounts

    def add_account(self, account):
        """
        Adds account to FAM system.
        :param account: a FamAccount.
        :return:
        """
        self.fam_accounts.append(account)

    def main_menu(self):
        """
        Display main menu functionality.

        Handles user inputs.
        :return:
        """
        while True:
            print("Main Menu\n"
                  "---------------\n"
                  "1. Register\n"
                  "2. Login\n"
                  "3. Exit\n")
            user_input = input("Enter action: ")
            if user_input == '1':
                self.register()
            elif user_input == '2':
                self.login_menu()
            elif user_input == '3':
                quit(1)
            else:
                print("Invalid input.\n")

    def login_menu(self):
        """
        Displays login menu.

        Handles user input.
        :return:
        """
        while True:
            print("Main Menu")
            count = 0
            for account in self.fam_accounts:
                count += 1
                user = account.get_user()
                print(f"{count}. {user.username} ({user.user_type})")
            print(f"{len(self.fam_accounts) + 1}. Back to main menu.")
            user_input = int(input("Enter action: ").strip()) - 1
            if int(user_input) in range(len(self.fam_accounts)):
                account = self.fam_accounts[int(user_input)]
                if account.get_user().get_lockout_check():
                    print("The account is lockout.")
                    return self.main_menu()
                else:
                    self.display_menu(account)
            elif int(user_input) == len(self.fam_accounts):
                return self.main_menu()
            else:
                print("Invalid input.\n")

    def register(self):
        """
        Registers a new user.
        :return:
        """
        username = input("Please enter the user name: ")
        age = input("Age: ")
        bank_number = input("Account number: ")
        bank_name = input("Bank name: ")
        bank_balance = float(input("Bank balance: "))
        bank_account = BankAccount(bank_balance, bank_name, bank_number)
        user = self.register_user_type(username, age)
        budgets = self.register_budget_dictionary(bank_balance)
        fam_account = FamAccount(user, bank_account, budgets)
        self.add_account(fam_account)
        print("Successfully register an account")

    def display_menu(self, account):
        """
        Displays menu.
        :return:
        """
        back_main_menu = False
        while True:
            print("Menu\n"
                  "---------------\n"
                  "1. View Budget\n"
                  "2. Record Transaction\n"
                  "3. View Transaction Record by Budget\n"
                  "4. View Bank Account Details\n"
                  "5. Log out\n")
            user_input = input("Enter action: ")
            if user_input == '1':
                self.view_budgets(account)
            elif user_input == '2':
                back_main_menu = account.create_new_transaction()
            elif user_input == '3':
                account.display_transaction_details()
            elif user_input == '4':
                print(account)
            elif user_input == '5':
                self.main_menu()
            else:
                print("Invalid input.\n")
            if back_main_menu:
                return

    @staticmethod
    def view_budgets(account):
        """
        Views budgets.
        :param account: a FamAccount
        :return:
        """
        for budget in account.budgets.values():
            print(budget)

    @staticmethod
    def register_user_type(username, age):
        """
        Registers a new user the FamAccount.
        :return:
        """
        while True:
            print("\nUser Type:\n"
                  "---------------\n"
                  "1. Trouble maker\n"
                  "2. Angel\n"
                  "3. Rebel\n")
            user_input = input("Enter action: ")
            if user_input == '1':
                user_type = Troublemaker()
                user = User(username, age, user_type)
                return user
            elif user_input == '2':
                user_type = Angel()
                user = User(username, age, user_type)
                return user
            elif user_input == '3':
                user_type = Rebel()
                user = User(username, age, user_type)
                return user
            else:
                print("Invalid input.\n")

    @staticmethod
    def register_budget_dictionary(balance):
        """
        Registers a budget dictionary.
        :param balance: a float
        :return: a dict
        """
        budgets = {}
        for cate in BudgetCategory:
            while True:
                if cate == BudgetCategory.Miscellaneous:
                    print(f"\nAllocating remaining balance to Miscellaneous Budget: ${balance}")
                    budgets[cate.name] = Budget(balance, cate.value)
                    break
                print(f"\nCurrent balance: ${balance}")
                print(f"{cate.name}")
                amount_allocated = float(input("Money deposit: "))
                if balance - amount_allocated > 0:
                    balance -= float(amount_allocated)
                    budgets[cate.name] = Budget(amount_allocated, cate.value)
                    break
                else:
                    print(f"\nInvalid amount: {amount_allocated}")
        return budgets
