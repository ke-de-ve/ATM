from typing import List
from .Account import  Account

class Bank:
    def __init__(self):
        self.accounts = []

    # add new account
    def add_account1(self, acc):
        self.accounts.append(acc)

    # add new account interactively
    def add_account(self):
        print("adding account...  ")
        x_name = str(input("what is your name? "))
        x_pin = int(input("what is your PIN? "))
        # Check if account already exists
        current = self.find_account(x_name, x_pin)
        if current is None:
            # if account doesn't exists yet create it and add to the back's accounts list
            current = Account(x_name, self.get_new_account_number(), 0.0, x_pin)
            self.accounts.append(current)
        else:
            # else let user know this account already exists
            print(current.name, ", you already have an account! Your balance is", current.balance)
        # return new or existing account
        return current

    # Find (Login) into account with User name and pin
    def find_account(self, name, pin):
        for acc in self.accounts:
            if acc.name == name and acc.pin == pin:
                return acc
        return None

    # find account by account number
    def find_account1(self, acc_number):
        for acc in self.accounts:
            if acc_number == acc.acc_number:
                return acc
        return None

    # generate new account number
    def get_new_account_number(self):
        res = 0
        for acc in self.accounts:
            if res < acc.acc_number:
                res = acc.acc_number
        res += 1
        return res

    # Transfer amount between 2 accounts:
    # from account acc_origin
    # to account with account_number = dest_acc_number
    def transfer(self, acc_origin, dest_acc_number, amount):
        # Check if amount is negative (don't allow users to transfer from other accounts)
        if amount < 0:
            print("ALERT! you can't transfer negative funds!")
            return;

        # Check if enough funds for transfer
        if acc_origin.balance < amount:
            print("you don't have enough funds for transfer!")
            return;

        # find account of destination
        acc_dest = self.find_account1(dest_acc_number)

        # Check if account was found and only then do transfer
        if acc_dest is None:
            print("unable to find account of destination:", dest_acc_number)
            return

        # if all is OK then transfer funds
        acc_origin.balance -= amount
        acc_dest.balance += amount

