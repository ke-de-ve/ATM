from typing import List
from .Account import  Account

class Bank:
    def __init__(self):
        self.accounts = List[Account]

    def add_account(self, acc):
        self.accounts.append(acc)
    
    def find_account(self, name, pin):
        for acc in self.accounts:
            if (acc.name == name and acc.pin == pin):
                return acc
        return None

    
        
