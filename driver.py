"""
This module is the driver for the FAM System.
"""
from fam_account import FamAccount
from bank_account import BankAccount
from troublemaker import Troublemaker
from rebel import Rebel
from budget import Budget
from user import User
from budget import BudgetCategory
from bank_fam_system import BankFamSystem


def load_test_account(system):
    """
    Creates a test FamAccount.
    :return: a FamAccount
    """
    user = User("Someone", 18, Troublemaker())
    b1 = BudgetCategory.GamesAndEntertainment
    b2 = BudgetCategory.ClothingAndAccessories
    b3 = BudgetCategory.Food
    b4 = BudgetCategory.Miscellaneous
    budgets = {b1.name: Budget(500, 1), b2.name: Budget(500, 2), b3.name: Budget(500, 3), b4.name: Budget(500, 4)}
    account = BankAccount(2000, "TD", "A123")
    fam_account = FamAccount(user, account, budgets)
    system.add_account(fam_account)
    user = User("One", 18, Rebel())
    fam_account_1 = FamAccount(user, account, budgets)
    system.add_account(fam_account_1)


def main():
    system = BankFamSystem()
    load_test_account(system)
    system.main_menu()


if __name__ == '__main__':
    main()
